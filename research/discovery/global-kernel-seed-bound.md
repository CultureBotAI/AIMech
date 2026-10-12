# Curator derivation: singleton removal preserves the fast error bound

The 2009 paper's Algorithm 2 removes seed n from its old cluster before using it as a new singleton. This changes that old cluster's mean. The bound in IV-A nevertheless extends to this initialization when cluster weights remain positive and the local updates are well-defined.

Use an RKHS, observation weights a_i>0, and an old cluster C of weight W with mean mu. The seed has weight a<W and centered vector z=phi(x_n)-mu. Removing it shifts the mean by delta=-a*z/(W-a). Compare with the hypothetical nearest-center assignment that retains all old means and adds phi(x_n). Its error is E_old-b_n (assuming old assigned distances are nearest-center distances, as after converged local fitting).

Within C, let R be those assigned to the new seed in that hypothetical comparison, choosing the seed itself to join R in a tie. Write B=sum_{i in R} a_i, so B>=a. Each i in R obeys 2*<phi(x_i)-mu,z> >= ||z||^2. The old weighted centered vectors sum to zero. For S=C\R, the change in cost from evaluating their distances at mu+delta rather than mu is

Delta = -2*a/(W-a) * sum_{i in R} a_i*<phi(x_i)-mu,z>
        + (W-B)*a^2/(W-a)^2 * ||z||^2
      <= a*W*(a-B)/(W-a)^2 * ||z||^2 <= 0.

All other old clusters retain their means, and R retains the seed center. Thus this comparison assignment costs at most E_old-b_n with the actual initialized centers. The actual nearest-center reassignment can only lower this cost, as can weighted-mean recomputation and further exact Lloyd steps. The argument also covers z=0. It does not resolve empty-cluster policies, non-PSD similarities, arbitrary approximate updates, or arbitrary empty-cluster repair. If an old source cluster is a singleton (a=W), the displayed initialization itself needs a convention.

This is a curator derivation of a source-supported claim, not source text or a historical code reproduction. A separate seeded unweighted two-dimensional probe found no counterexample in 10,000 datasets under defined nonempty runs; that finite probe alone is not a proof.
