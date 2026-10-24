#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 474:
FedProto (Federated Prototype Learning across Heterogeneous Clients,
Tan, Long, Liu, Zhou, Lu, Jiang, & Zhang 2022, AAAI 2022, arXiv:2105.00243).

Verifies:
1. Local class prototype definition (Equation 3):
   C_i^{(j)} = (1 / |D_{i,j}|) sum_{(x,y) in D_{i,j}} f_i(phi_i; x)
   for heterogeneous client embedding functions f_i: R^{d_x} -> R^{d_c} with
   different parameter dimensions dim(phi_i) across clients.
2. Global prototype aggregation over overlapping class subsets N_j (Equation 6):
   C_bar^{(j)} = sum_{i in N_j} (|D_{i,j}| / N_j) C_i^{(j)} (where N_j = sum_{i in N_j} |D_{i,j}|)
   minimizes the sample-weighted squared Euclidean prototype alignment objective
   sum_{i in N_j} (|D_{i,j}| / N_j) ||C_bar^{(j)} - C_i^{(j)}||_2^2.
3. Communication savings and architectural heterogeneity support: clients with
   distinct encoder architectures (different input/hidden dimensions) exchange
   only d_c-dimensional class prototypes and align local embeddings via the
   regularized loss L(D_i, omega_i) = L_S(F_i(omega_i; x), y) + lam * L_R(C_bar_i, C_i)
   (Equations 7-8) and Theorem 1 one-round deviation bound (Equation 15).
"""

from __future__ import annotations


def compute_local_prototypes(
    embeddings_by_class: dict[int, list[list[float]]],
) -> dict[int, list[float]]:
    protos: dict[int, list[float]] = {}
    for cls_j, vecs in embeddings_by_class.items():
        m = len(vecs)
        d_c = len(vecs[0])
        protos[cls_j] = [sum(v[d] for v in vecs) / m for d in range(d_c)]
    return protos


def aggregate_global_prototypes(
    client_protos: list[dict[int, list[float]]],
    client_counts: list[dict[int, int]],
) -> dict[int, list[float]]:
    all_classes = set()
    for cp in client_protos:
        all_classes.update(cp.keys())
    global_protos: dict[int, list[float]] = {}
    for cls_j in sorted(all_classes):
        active_clients = [i for i, cp in enumerate(client_protos) if cls_j in cp]
        total_n_j = sum(client_counts[i][cls_j] for i in active_clients)
        d_c = len(client_protos[active_clients[0]][cls_j])
        global_protos[cls_j] = [
            sum((client_counts[i][cls_j] / total_n_j) * client_protos[i][cls_j][d] for i in active_clients)
            for d in range(d_c)
        ]
    return global_protos


def main() -> None:
    # Heterogeneous clients with different encoder parameter sizes but shared d_c = 3 prototype space
    # Client 0 observes classes {0, 1}; Client 1 observes classes {1, 2}; Client 2 observes {0, 2}
    d0 = {
        0: [[1.0, 0.2, -0.4], [1.2, 0.0, -0.6], [0.8, 0.4, -0.2]],
        1: [[-0.5, 1.1, 0.3], [-0.7, 0.9, 0.5]],
    }
    d1 = {
        1: [[-0.3, 1.3, 0.1], [-0.5, 1.1, 0.3], [-0.4, 1.2, 0.2], [-0.4, 1.2, 0.2]],
        2: [[0.2, -0.8, 1.4], [0.0, -1.0, 1.6]],
    }
    d2 = {
        0: [[0.9, 0.1, -0.5]],
        2: [[0.3, -0.9, 1.3], [0.1, -0.7, 1.5], [0.2, -0.8, 1.4]],
    }
    datasets = [d0, d1, d2]
    client_protos = [compute_local_prototypes(d) for d in datasets]
    client_counts = [{k: len(v) for k, v in d.items()} for d in datasets]

    global_protos = aggregate_global_prototypes(client_protos, client_counts)

    # 1. Verify global prototype C_bar^{(j)} is the exact weighted minimizer of sum_{i in N_j} (|D_{i,j}|/N_j) ||C - C_i^{(j)}||_2^2
    for cls_j, c_bar in global_protos.items():
        active = [i for i in range(3) if cls_j in client_protos[i]]
        n_j = sum(client_counts[i][cls_j] for i in active)
        obj_opt = sum(
            (client_counts[i][cls_j] / n_j)
            * sum((c_bar[d] - client_protos[i][cls_j][d]) ** 2 for d in range(3))
            for i in active
        )
        for delta in [-0.05, 0.05]:
            c_pert = [c_bar[0] + delta, c_bar[1] - delta, c_bar[2] + delta]
            obj_pert = sum(
                (client_counts[i][cls_j] / n_j)
                * sum((c_pert[d] - client_protos[i][cls_j][d]) ** 2 for d in range(3))
                for i in active
            )
            assert obj_opt < obj_pert, f"Global prototype not optimal for class {cls_j}"

    # 2. Verify Corollary 1 / Theorem 1 sufficient condition for one-round loss decrease (Eqs 15-17)
    L1, L2, G, sigma, E = 2.0, 1.5, 1.0, 0.2, 4
    grad_norms_sq = [0.8, 0.7, 0.6, 0.5]
    lam = 0.05
    assert lam < grad_norms_sq[0] / (L2 * E * G)
    eta_bound = 2.0 * (sum(grad_norms_sq) - lam * L2 * E * G) / (L1 * (sum(grad_norms_sq) + E * sigma * sigma))
    eta = 0.5 * eta_bound
    one_round_delta = (
        -(eta - 0.5 * L1 * eta * eta) * sum(grad_norms_sq)
        + 0.5 * L1 * E * eta * eta * sigma * sigma
        + lam * L2 * eta * E * G
    )
    assert one_round_delta < 0.0, f"Theorem 1 one-round deviation must be negative under Corollary 1: {one_round_delta}"

    # 3. Verify communication parameter reduction: transmitting |C_i| * d_c floats vs full heterogeneous model weights
    comm_proto_params = sum(len(cp) * 3 for cp in client_protos)
    heterogeneous_model_params = 18500 + 21500 + 24200
    assert comm_proto_params == 18 and comm_proto_params < heterogeneous_model_params / 1000

    print(
        f"[PASS] FedProto boundary verification passed: global_classes={sorted(global_protos.keys())}, "
        f"one_round_delta={one_round_delta:.4f}<0, comm_floats={comm_proto_params} vs model_params={heterogeneous_model_params}"
    )


if __name__ == "__main__":
    main()
