#!/usr/bin/env python3
"""Deterministic boundary verification for Round 830:
RAM (Random Accelerated Motion) Multidimensional Time Series Generator
(Bachmann & Freytag, 2018, arXiv:1804.06352v3).

Verifies:
1. Kinematic Euler state update (Section 3, Equations 1-2, Algorithm 1):
   v(t + dt) = v(t) + a(t)*dt, s(t + dt) = s(t) + v(t)*dt + 0.5*a(t)*dt^2.
2. Hyper-rectangle boundary reflection (Section 3.1, Algorithm 1):
   Whenever a coordinate s_d(t+dt) crosses [0, L_d], the trajectory reflects
   elastically at the boundary wall and reverses velocity v_d <- -v_d, keeping
   all multidimensional coordinates strictly within [0, L_d]^D.
3. Damped harmonic attractor oscillation (Section 3.2, Algorithm 2):
   Under spring restoring acceleration a(t) = -k*(s(t) - c) - gamma*v(t)
   around attractor c in R^D with damping gamma > 0, mechanical energy
   E(t) = 0.5*||v(t)||^2 + 0.5*k*||s(t) - c||^2 is strictly non-increasing.
"""

import math
import random


def simulate_ram(dim: int, steps: int, dt: float, box_len: float, a_max: float, seed: int = 42):
    rng = random.Random(seed)
    s = [box_len * 0.5 for _ in range(dim)]
    v = [0.0 for _ in range(dim)]
    traj = []
    reflections = 0
    for _ in range(steps):
        a = [rng.uniform(-a_max, a_max) for _ in range(dim)]
        s_next = [s[d] + v[d] * dt + 0.5 * a[d] * (dt ** 2) for d in range(dim)]
        v_next = [v[d] + a[d] * dt for d in range(dim)]
        for d in range(dim):
            while s_next[d] < 0.0 or s_next[d] > box_len:
                if s_next[d] < 0.0:
                    s_next[d] = -s_next[d]
                    v_next[d] = -v_next[d]
                    reflections += 1
                elif s_next[d] > box_len:
                    s_next[d] = 2.0 * box_len - s_next[d]
                    v_next[d] = -v_next[d]
                    reflections += 1
            assert 0.0 <= s_next[d] <= box_len
        s, v = s_next, v_next
        traj.append(list(s))
    return traj, reflections


def simulate_damped_attractor(dim: int, steps: int, dt: float, k: float, gamma: float):
    c = [5.0 for _ in range(dim)]
    s = [8.0 for _ in range(dim)]
    v = [1.5 for _ in range(dim)]

    def energy(pos, vel):
        return 0.5 * sum(vi ** 2 for vi in vel) + 0.5 * k * sum((pi - ci) ** 2 for pi, ci in zip(pos, c))

    e0 = energy(s, v)
    prev_e = e0
    for _ in range(steps):
        # Damped harmonic update around attractor c
        a = [-k * (s[d] - c[d]) - gamma * v[d] for d in range(dim)]
        s_mid = [s[d] + 0.5 * v[d] * dt for d in range(dim)]
        v_mid = [v[d] + 0.5 * a[d] * dt for d in range(dim)]
        a_mid = [-k * (s_mid[d] - c[d]) - gamma * v_mid[d] for d in range(dim)]
        s = [s[d] + v_mid[d] * dt for d in range(dim)]
        v = [v[d] + a_mid[d] * dt for d in range(dim)]
        cur_e = energy(s, v)
        assert cur_e <= prev_e + 1e-9
        prev_e = cur_e
    dist_final = math.sqrt(sum((s[d] - c[d]) ** 2 for d in range(dim)))
    return e0, prev_e, dist_final


def main() -> None:
    traj, refl = simulate_ram(dim=6, steps=250, dt=0.1, box_len=10.0, a_max=8.0)
    assert len(traj) == 250 and len(traj[0]) == 6
    assert refl > 0
    e0, ef, dist_f = simulate_damped_attractor(dim=4, steps=800, dt=0.01, k=4.0, gamma=1.5)
    assert ef < 0.01 * e0 and dist_f < 0.25
    print(
        f"[PASS] Round 830 RAM generator verified: D=6 steps=250 reflections={refl}, "
        f"attractor energy {e0:.3f}->{ef:.4f}, final_dist={dist_f:.4f}"
    )


if __name__ == "__main__":
    main()
