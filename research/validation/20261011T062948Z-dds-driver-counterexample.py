"""Curator finite-tree transcription of Walsh 1997's printed DDS driver.

This is not execution of an author implementation or a general algorithm audit.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

children = {"root": ("L", "R"), "L": ("LL", "LR")}
goals = {"LR"}

def probe(node, k, visited):
    if node not in children:
        visited.append(node)
        return node in goals, 0
    left, right = children[node]
    if k == 0:
        goal, depth = probe(left, 0, visited)
        return goal, 1 + depth
    if k == 1:
        goal, depth = probe(right, 0, visited)
        return goal, 1 + depth
    goal, depth1 = probe(left, k - 1, visited)
    if goal:
        return goal, 1 + depth1
    goal, depth2 = probe(right, k - 1, visited)
    return goal, 1 + max(depth1, depth2)

def run(retain_observed_maximum=False):
    k = 0
    observed_maximum = 0
    trace = []
    while True:
        visited = []
        goal, depth = probe("root", k, visited)
        observed_maximum = max(observed_maximum, depth)
        trace.append({"iteration": k, "leaves": visited,
                      "returned_depth": depth, "goal_found": goal})
        k += 1
        bound = observed_maximum if retain_observed_maximum else depth
        if goal or k > bound:
            return {"goal_found": goal, "trace": trace,
                    "stopping_comparison": [k, bound]}

printed = run()
modified = run(True)
assert printed["goal_found"] is False
assert modified["goal_found"] is True
result = {
    "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "source": "https://www.ijcai.org/Proceedings/97-2/Papers/086.pdf",
    "locator": "Printed p. 1389 / PDF p. 2, DDS driver and PROBE",
    "authorship": "Curator transcription and finite-tree illustration",
    "tree": children,
    "goal_leaves": sorted(goals),
    "literal_driver": printed,
    "curator_variant_retaining_observed_maximum": modified,
    "interpretation": "The printed driver overwrites the returned depth each iteration. On this finite unbalanced binary tree, it stops after visiting LL and R and misses goal LR. Retaining the maximum depth observed across passes finds LR in this example.",
    "limitations": [
        "This is not execution of the author's reference implementation.",
        "The one-tree success of the curator variant is not a general correctness proof or an author-approved correction.",
        "The source prose refers to the deepest leaf, while the printed driver uses the depth returned by the current probe. The discrepancy is preserved rather than silently repaired."
    ],
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
print(json.dumps(result, indent=2))
