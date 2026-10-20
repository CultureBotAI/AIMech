# Discovery Report: Round 746 — TART (Task-Aware Retrieval with Instructions)

- **Timestamp**: `2026-10-19T13:49:00Z`
- **Selected Concept**: `AIMech:TARTTaskAwareRetrievalWithInstructions` (*TART (Task-Aware Retrieval with Instructions)*)
- **Record Path**: `data/curated/TARTTaskAwareRetrievalWithInstructions.yaml`
- **Primary Source**: Akari Asai, Timo Schick, Patrick Lewis, Xilun Chen, Gautier Izacard, Sebastian Riedel, Hannaneh Hajishirzi, Wen-tau Yih — *Task-aware Retrieval with Instructions* (`https://dblp.org/search/publ/api?q=Task-aware+Retrieval+with+Instructions+Asai&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Asai, Schick, Lewis, Chen, Izacard, Riedel, Hajishirzi, and Yih (Findings of ACL 2023, pp. 3994-4022, arXiv:2211.09260). Distinguished from standard zero-shot dense retrievers (such as Contriever or GTR) that condition only on the query q, from UPR (Sachan et al., 2022) which uses a fixed question-generation prompt to compute log p(q | d) rather than adapting relevance to arbitrary task instructions t, and from Promptagator (Dai et al., 2023) which trains separate task-specific retrievers on LLM-generated synthetic queries.

## Constructed Boundary & Regime Verification

```text
TART boundary verification passed: {'loss_before': 0.2204, 'loss_after': 0.0}
```
