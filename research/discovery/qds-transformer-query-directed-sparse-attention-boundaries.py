#!/usr/bin/env python3
"""Constructed boundary verification for QDS-Transformer (Jiang et al., Findings of EMNLP 2020, arXiv:2010.12683)."""


def build_qds_adjacency(
    n_tokens: int,
    w: int,
    cls_idx: int,
    query_indices: set[int],
    sos_indices: set[int],
) -> list[list[int]]:
    """Eqs. (7)-(10): Construct A_QDS = A_local U A_sent U A_query U A_[CLS]."""
    adj = [[0] * n_tokens for _ in range(n_tokens)]
    half_w = w // 2
    for i in range(n_tokens):
        for j in range(n_tokens):
            # Eq. (7): Local windowed attention |i - j| <= w / 2
            is_local = abs(i - j) <= half_w
            # Eq. (8): Hierarchical sentence attention on [SOS] tokens
            is_sent = (j in sos_indices) or (i in sos_indices)
            # Eq. (9): Query-directed global attention on query tokens
            is_query = (i in query_indices) or (j in query_indices)
            # Eq. (10): Global [CLS] attention
            is_cls = (i == cls_idx) or (j == cls_idx)
            if is_local or is_sent or is_query or is_cls:
                adj[i][j] = 1
    return adj


def build_local_only_adjacency(n_tokens: int, w: int) -> list[list[int]]:
    """Eq. (7) alone: Sparse Transformer local attention."""
    adj = [[0] * n_tokens for _ in range(n_tokens)]
    half_w = w // 2
    for i in range(n_tokens):
        for j in range(n_tokens):
            if abs(i - j) <= half_w:
                adj[i][j] = 1
    return adj


def main() -> None:
    # Construct a sequence of length n=100 with local window w=8:
    # Index 0: [CLS], Indices 1..3: Query tokens, Indices 4, 30, 65: [SOS] sentence boundary tokens
    n = 100
    w = 8
    cls_idx = 0
    query_indices = {1, 2, 3}
    sos_indices = {4, 30, 65}

    adj_qds = build_qds_adjacency(n, w, cls_idx, query_indices, sos_indices)
    adj_local = build_local_only_adjacency(n, w)

    # 1. Sparsity check: QDS-Transformer uses a small fraction of full n^2 = 10,000 edges:
    total_dense = n * n
    nnz_qds = sum(sum(row) for row in adj_qds)
    nnz_local = sum(sum(row) for row in adj_local)
    assert nnz_local < nnz_qds < total_dense * 0.25

    # 2. Query-directed global connectivity: distant document token (e.g., i=85) directly attends to query token (j=2)
    # and sentence boundary [SOS] token (j=65), whereas local-only attention cannot:
    assert adj_local[85][2] == 0, "Local attention cannot reach query token from position 85"
    assert adj_qds[85][2] == 1, "QDS attention connects every document token to query tokens"
    assert adj_local[85][65] == 0, "Local attention cannot reach [SOS] at 65 from position 85"
    assert adj_qds[85][65] == 1, "QDS attention connects every token to [SOS] sentence tokens"

    # 3. Distant non-SOS document tokens (e.g., i=20 and j=85) remain disconnected in A_QDS:
    assert adj_qds[20][85] == 0, "Distant non-query, non-SOS document tokens are pruned for sparsity"

    print("QDS-Transformer boundary verification passed:")
    print(f"  Dense edges: {total_dense}, QDS edges: {nnz_qds} ({100.0 * nnz_qds / total_dense:.2f}%), "
          f"Local-only edges: {nnz_local}")
    print(f"  A_QDS[85,2]={adj_qds[85][2]}, A_QDS[85,65]={adj_qds[85][65]}, A_QDS[20,85]={adj_qds[20][85]}")


if __name__ == "__main__":
    main()
