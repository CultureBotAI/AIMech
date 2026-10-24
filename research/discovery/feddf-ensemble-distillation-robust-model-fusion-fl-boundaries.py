#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 407:
FedDF: Ensemble Distillation for Robust Model Fusion in Federated Learning
(Lin, Kong, Stich, & Jaggi, NeurIPS 2020, Vol. 33, pp. 2351-2363).
"""

import math
import random


def sigmoid(z):
    if z >= 0.0:
        return 1.0 / (1.0 + math.exp(-z))
    ez = math.exp(z)
    return ez / (1.0 + ez)


def relu(z):
    return z if z > 0.0 else 0.0


def main():
    rng = random.Random(407)

    # 1. Homogeneous non-linear model fusion (Algorithm 1):
    # Two clients learn 2-hidden-unit ReLU networks f(x) = sum_{j=1}^2 a_j * ReLU(w_j^T x + b_j) + b_out
    # that represent the exact same non-linear band target function up to hidden-unit permutation.
    # Direct coordinate averaging (FedAvg) collapses the opposing hidden weight vectors to 0,
    # whereas FedDF (distilling the ensemble average logit via KL divergence) recovers the ensemble predictor.
    client1_units = [
        ([4.0, 4.0], -1.0, 5.0),
        ([-4.0, -4.0], -1.0, 5.0),
    ]
    client2_units = [
        ([-4.0, -4.0], -1.0, 5.0),
        ([4.0, 4.0], -1.0, 5.0),
    ]
    bias_out = -2.5

    def eval_net(units, b_out, x):
        s = b_out
        for w, b, a in units:
            s += a * relu(w[0] * x[0] + w[1] * x[1] + b)
        return s

    # Coordinate parameter average (FedAvg): w_avg = [0, 0] -> completely collapses hidden units!
    fedavg_units = [
        (
            [0.5 * (client1_units[j][0][0] + client2_units[j][0][0]),
             0.5 * (client1_units[j][0][1] + client2_units[j][0][1])],
            0.5 * (client1_units[j][1] + client2_units[j][1]),
            0.5 * (client1_units[j][2] + client2_units[j][2]),
        )
        for j in range(2)
    ]

    # Unlabeled server distillation dataset D_proxy
    proxy_X = [[rng.uniform(-1.5, 1.5), rng.uniform(-1.5, 1.5)] for _ in range(160)]
    teacher_probs = []
    for x in proxy_X:
        logit_ens = 0.5 * (eval_net(client1_units, bias_out, x) + eval_net(client2_units, bias_out, x))
        teacher_probs.append(sigmoid(logit_ens))

    # Distill into student network via KL divergence gradient steps (Algorithm 1)
    student_units = [
        ([2.0, 1.8], -0.6, 3.0),
        ([-1.9, -2.1], -0.6, 3.0),
    ]
    student_b = -1.5
    lr = 0.35
    for _ in range(500):
        gw = [[0.0, 0.0], [0.0, 0.0]]
        gb = [0.0, 0.0]
        ga = [0.0, 0.0]
        gb_out = 0.0
        n = len(proxy_X)
        for idx, x in enumerate(proxy_X):
            p_t = teacher_probs[idx]
            z_s = eval_net(student_units, student_b, x)
            p_s = sigmoid(z_s)
            dz = (p_s - p_t) / n
            gb_out += dz
            for j in range(2):
                w, b, a = student_units[j]
                pre = w[0] * x[0] + w[1] * x[1] + b
                h = relu(pre)
                ga[j] += dz * h
                if pre > 0.0:
                    gb[j] += dz * a
                    gw[j][0] += dz * a * x[0]
                    gw[j][1] += dz * a * x[1]
        student_b -= lr * gb_out
        for j in range(2):
            w, b, a = student_units[j]
            student_units[j] = (
                [w[0] - lr * gw[j][0], w[1] - lr * gw[j][1]],
                b - lr * gb[j],
                a - lr * ga[j],
            )

    def kl_bernoulli(p, q):
        q = max(1e-12, min(1.0 - 1e-12, q))
        res = 0.0
        if p > 1e-12:
            res += p * math.log(p / q)
        if 1.0 - p > 1e-12:
            res += (1.0 - p) * math.log((1.0 - p) / (1.0 - q))
        return res

    kl_fedavg = sum(
        kl_bernoulli(teacher_probs[i], sigmoid(eval_net(fedavg_units, bias_out, proxy_X[i])))
        for i in range(len(proxy_X))
    ) / len(proxy_X)
    kl_feddf = sum(
        kl_bernoulli(teacher_probs[i], sigmoid(eval_net(student_units, student_b, proxy_X[i])))
        for i in range(len(proxy_X))
    ) / len(proxy_X)

    assert kl_feddf < 0.01 and kl_fedavg > 1.0 and kl_feddf < 0.01 * kl_fedavg, (
        f"Expected kl_feddf << kl_fedavg, got kl_feddf={kl_feddf}, kl_fedavg={kl_fedavg}"
    )

    # 2. Heterogeneous model fusion (Algorithm 3): fuse a 2-unit model and a 4-unit model into a quadratic polynomial student
    # via logit ensemble distillation (impossible for coordinate-averaging FedAvg)
    het_teacher_units = client1_units + [([2.5, 2.5], -1.2, 2.0), ([-2.5, -2.5], -1.2, 2.0)]
    het_probs = [
        sigmoid(0.5 * (eval_net(client1_units, bias_out, x) + eval_net(het_teacher_units, -2.5, x)))
        for x in proxy_X
    ]
    theta_quad = [-2.0, 0.0, 0.0, 2.0]
    for _ in range(300):
        g_q = [0.0] * 4
        for idx, x in enumerate(proxy_X):
            feats = [1.0, x[0], x[1], (x[0] + x[1]) ** 2]
            p_s = sigmoid(sum(theta_quad[c] * feats[c] for c in range(4)))
            dz = (p_s - het_probs[idx]) / len(proxy_X)
            for c in range(4):
                g_q[c] += dz * feats[c]
        theta_quad = [theta_quad[c] - 0.8 * g_q[c] for c in range(4)]

    kl_het_student = sum(
        kl_bernoulli(
            het_probs[i],
            sigmoid(
                theta_quad[0]
                + theta_quad[1] * proxy_X[i][0]
                + theta_quad[2] * proxy_X[i][1]
                + theta_quad[3] * ((proxy_X[i][0] + proxy_X[i][1]) ** 2)
            ),
        )
        for i in range(len(proxy_X))
    ) / len(proxy_X)
    assert kl_het_student < 0.06, f"Expected kl_het_student < 0.06, got {kl_het_student}"

    print(
        f"[PASS] Round 407 FedDF (Lin et al. 2020): "
        f"kl_feddf={kl_feddf:.5f}<<kl_fedavg={kl_fedavg:.4f}, "
        f"kl_het_student={kl_het_student:.5f}"
    )


if __name__ == "__main__":
    main()
