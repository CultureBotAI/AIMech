#!/usr/bin/env python3
"""Constructed boundary verification for CLEAR (Gao et al., ECIR 2021, arXiv:2004.13969).

Verifies:
1. Residual-based hinge margin m_r(s_lex(q, d+), s_lex(q, d-)) = xi - lambda_train * (s_lex(q, d+) - s_lex(q, d-))
   (Eq. 6) and residual hinge loss L = [m_r - s_emb(q, d+) + s_emb(q, d-)]_+ (Eq. 7):
   - When BM25 already ranks d+ far above d-, m_r <= 0 and the embedding model receives zero gradient
     when s_emb(q, d+) >= s_emb(q, d-).
   - When BM25 fails (lexical error where s_lex(q, d-) > s_lex(q, d+)), m_r > xi increases dynamically
     in proportion to the lexical error magnitude, driving the embedding model to compensate.
2. Test-time complementary scoring s_CLEAR(q, d) = lambda_test * s_lex(q, d) + s_emb(q, d) (Eq. 8).
"""

from __future__ import annotations


def residual_margin(
    s_lex_pos: float,
    s_lex_neg: float,
    xi: float = 1.0,
    lambda_train: float = 0.1,
) -> float:
    """Implements Eq. (6): m_r(s_lex(q, d+), s_lex(q, d-)) = xi - lambda_train * (s_lex(q, d+) - s_lex(q, d-))."""
    return xi - lambda_train * (s_lex_pos - s_lex_neg)


def residual_hinge_loss(
    s_lex_pos: float,
    s_lex_neg: float,
    s_emb_pos: float,
    s_emb_neg: float,
    xi: float = 1.0,
    lambda_train: float = 0.1,
) -> float:
    """Implements Eq. (7): L = max(0, m_r(s_lex(q, d+), s_lex(q, d-)) - s_emb(q, d+) + s_emb(q, d-))."""
    m_r = residual_margin(s_lex_pos, s_lex_neg, xi=xi, lambda_train=lambda_train)
    return max(0.0, m_r - s_emb_pos + s_emb_neg)


def clear_score(s_lex: float, s_emb: float, lambda_test: float = 0.5) -> float:
    """Implements Eq. (8): s_CLEAR(q, d) = lambda_test * s_lex(q, d) + s_emb(q, d)."""
    return lambda_test * s_lex + s_emb


def main() -> None:
    xi = 1.0
    lambda_train = 0.1
    lambda_test = 0.5

    # Case 1: Easy lexical pair where BM25 already succeeds strongly (s_lex(d+) = 18.0 >> s_lex(d-) = 4.0)
    m_r_easy = residual_margin(18.0, 4.0, xi=xi, lambda_train=lambda_train)
    assert abs(m_r_easy - (-0.4)) < 1e-9 and m_r_easy < 0.0
    # Even with a modest embedding margin (s_emb_pos = 2.0, s_emb_neg = 1.9), loss is 0 (no wasted capacity):
    loss_easy = residual_hinge_loss(18.0, 4.0, 2.0, 1.9, xi=xi, lambda_train=lambda_train)
    assert loss_easy == 0.0

    # Case 2: Lexical failure due to vocabulary mismatch (Table 3: "weather in danville, ca" vs "Sunny, rain, wind")
    # Error-based negative d- has exact lexical overlap ("weather") so s_lex(d-) = 11.5 > s_lex(d+) = 3.5:
    s_lex_pos_hard = 3.5
    s_lex_neg_hard = 11.5
    m_r_hard = residual_margin(s_lex_pos_hard, s_lex_neg_hard, xi=xi, lambda_train=lambda_train)
    # Residual margin expands above xi = 1.0 to 1.8:
    assert abs(m_r_hard - 1.8) < 1e-9 and m_r_hard > xi

    # Static-margin model (m = 1.0) stops updating once s_emb(d+) - s_emb(d-) = 1.2:
    s_emb_pos_static = 4.2
    s_emb_neg_static = 3.0
    static_loss = max(0.0, 1.0 - s_emb_pos_static + s_emb_neg_static)
    assert static_loss == 0.0
    # Yet at test time with lambda_test = 0.5, static-margin embedding margin (1.2) is NOT enough
    # to overcome the lexical deficit 0.5 * (3.5 - 11.5) = -4.0!
    # In contrast, CLEAR's residual margin forces s_emb(d+) - s_emb(d-) to grow to compensate:
    res_loss_at_static = residual_hinge_loss(
        s_lex_pos_hard, s_lex_neg_hard, s_emb_pos_static, s_emb_neg_static, xi=xi, lambda_train=lambda_train
    )
    assert res_loss_at_static > 0.0

    # After residual training drives semantic embedding margin above the lexical gap (e.g. s_emb_pos = 8.5, s_emb_neg = 3.0):
    s_emb_pos_clear = 8.5
    s_emb_neg_clear = 3.0
    clear_pos = clear_score(s_lex_pos_hard, s_emb_pos_clear, lambda_test=lambda_test)
    clear_neg = clear_score(s_lex_neg_hard, s_emb_neg_clear, lambda_test=lambda_test)
    assert clear_pos > clear_neg

    print(
        f"[PASS] CLEAR boundaries verified: m_r_easy={m_r_easy:.2f} (loss={loss_easy:.2f}), "
        f"m_r_hard={m_r_hard:.2f} > xi={xi:.2f}, clear_pos={clear_pos:.2f} > clear_neg={clear_neg:.2f}"
    )


if __name__ == "__main__":
    main()
