# Flattened slice sampling discovery — 2026-10-14T21:38:22Z

Two finite DRAFT conditional sampling algorithms were created with related AIO Markov Chain mappings.

## Flattened slice sampling

`AIMech:FlattenedSliceSampling` — `data/curated/FlattenedSliceSampling.yaml`

A finite categorical conditional-update algorithm that splits excess probability from a maximum-probability state into additional bars and samples a directed move to the preceding bar intersecting a random height, while retaining the given state order.

## Zero-self flattened slice sampling

`AIMech:ZeroSelfFlattenedSliceSampling` — `data/curated/ZeroSelfFlattenedSliceSampling.yaml`

A finite categorical conditional-update algorithm that flattens probability bars and relocates a qualifying blocker before the maximum-probability state, yielding directed slice transitions with the minimum permitted self-transition probability.

## Evidence and scope

FSS retains the supplied label order, including zero-probability labels. ZFSS uses a qualifying blocker relocation. The shared dominant-mass and zero-current branches do not make the general kernels identical. Target invariance does not guarantee irreducibility, aperiodicity or improved runtime.

The author-hosted report dated 26 March 2024 was selectively read. Its printed Figure 10 ZFSS matrix fails stationarity; the raw matrix and first failed comparison remain in the provenance. Algorithm 8 and independently derived bar geometry support the curated kernels. Algorithm 9 has an explicit loop interpretation and closed-endpoint caveat; no silent source repair or author erratum is claimed.

Two portable sibling scripts retain exact rational curator calculations and saved outputs. Original scripts, results, derivative changes, execution receipts and source-error lineage are preserved in the JSON. These bounded checks are not author-code execution, benchmark replication or universal proofs. Root and supporting-agent reading scopes are separately attributed within the same author workflow.

Current canonical bytes and normalized identities were refreshed; four complete checkouts were searched including ignored and hidden files. The 891 prior main frontier entries gain two actual record leaves, totaling 893, with all 393 nested entries unchanged. The existing Neal2024 source-family lead remains partially addressed. Other labels remain open research, and no saturation is claimed.

Full structured ledger: `research/discovery/20261014T213822Z-flattened-slice-sampling.json`

Record objects were structurally validated before creation. Full gates, actual saved reviews and publication remain later work.
