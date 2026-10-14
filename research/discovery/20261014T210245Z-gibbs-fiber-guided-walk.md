# Gibbs, fiber and guided-walk discovery — 2026-10-14T21:02:45Z

Three narrow DRAFT sampling algorithms were created with primary method evidence and related AIO Markov Chain mappings.

## Liu modified discrete-state Gibbs sampler

`AIMech:LiuModifiedGibbsSampler` — `data/curated/LiuModifiedGibbsSampler.yaml`

A discrete conditional sampling algorithm that proposes a category from the full conditional distribution with the current category excluded, then applies a Metropolis correction to preserve the original conditional distribution.

## Diaconis–Holmes–Neal fiber sampler

`AIMech:DiaconisHolmesNealFiberSampler` — `data/curated/DiaconisHolmesNealFiberSampler.yaml`

A finite-state Metropolis sampler that uses partitions into ordered lines, retains a binary direction for each partition, and combines a neighbor proposal with a separate probabilistic sign update to preserve a target distribution on the augmented state.

## Gustafson guided-walk Metropolis sampler

`AIMech:GustafsonGuidedWalkMetropolis` — `data/curated/GustafsonGuidedWalkMetropolis.yaml`

A continuous-state Metropolis sampler that augments a univariate state with a binary direction, proposes a half-normal displacement along that direction, retains direction after acceptance and reverses it after rejection.

## Evidence and scope

Liu’s original 1996 PDF remains inaccessible; the mechanism uses Neal’s inspected 2004 mathematical treatment. DHN evidence is the 5 June 1997 report, with the one-line directed case included in the finite fiber identity. Gustafson evidence is the 1998 journal-layout PDF from a public mirror; contradictory performance-rate labels are not adopted as numerical claims.

Exact source URLs, hashes, separate root/agent reading scopes, identity and frontier assessments, and bounded mathematical audits are retained in the JSON ledger. Curator calculations are independent illustrations, not author-code execution, benchmark replication or general proofs.

All current canonical bytes and normalized identities, plus ignored-inclusive searches of four full checkouts, were refreshed before exclusive writes. The main frontier carries 888 entries and adds 3 actual records, for 891; all 393 nested entries remain unchanged. Existing source refinements were resolved in place; no duplicate pending leaves or standalone directed specialization were added. Remaining scopes stay open, and no saturation is claimed.

Full structured ledger: `research/discovery/20261014T210245Z-gibbs-fiber-guided-walk.json`

Record objects were structurally validated before creation. Full project gates, canonical scientific reviews and publication checks are later work.
