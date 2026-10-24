#!/usr/bin/env python3
"""Constructed boundary verification for Data Persistence Bias (Elmas, WebSci 2023, arXiv:2303.00902)."""

import json


def compute_turnout_and_orientation_bias(records):
    """Compute Tweet Turnout, Author Turnout, and Political Orientation shift (Section 3, pp. 3-4)."""
    n_orig = len(records)
    orig_authors = {r["author_id"] for r in records}
    recollected = [r for r in records if r["persisted"]]
    n_rec = len(recollected)
    rec_authors = {r["author_id"] for r in recollected}

    tweet_turnout = n_rec / n_orig
    author_turnout = len(rec_authors) / len(orig_authors)

    mean_orig = sum(r["orientation"] for r in records) / n_orig
    mean_rec = sum(r["orientation"] for r in recollected) / n_rec
    orientation_shift = mean_rec - mean_orig
    return {
        "tweet_turnout": tweet_turnout,
        "author_turnout": author_turnout,
        "mean_orig": mean_orig,
        "mean_rec": mean_rec,
        "orientation_shift": orientation_shift,
    }


def main():
    # Construct synthetic dataset where hyperactive right-leaning accounts (+2.5) are suspended
    # at higher rates than moderate/left-leaning accounts (-0.8), matching Section 4 findings
    records = []
    # 40 moderate/left authors posting 2 posts each (80 posts), 75% persistence
    for i in range(40):
        persisted = (i % 4) != 0
        for p in range(2):
            records.append({"author_id": f"left_{i}", "orientation": -0.8, "persisted": persisted, "frame": "hero"})

    # 10 hyperactive right-aligned authors posting 8 posts each (80 posts), only 20% persistence due to suspension
    for i in range(10):
        persisted = i < 2
        for p in range(8):
            records.append({"author_id": f"right_{i}", "orientation": 2.4, "persisted": persisted, "frame": "threat"})

    stats = compute_turnout_and_orientation_bias(records)

    # Verify author turnout > tweet turnout when hyperactive accounts are disproportionately removed
    assert stats["author_turnout"] > stats["tweet_turnout"] + 0.10
    # Verify retrospective recollection shifts mean political orientation significantly leftward (< 0)
    assert stats["mean_orig"] > 0.70
    assert stats["mean_rec"] < -0.10
    assert stats["orientation_shift"] < -0.80

    # Verify frame-specific turnout disparity (Section 6: "threat" frame suffers lower turnout than "hero" frame)
    threat_orig = [r for r in records if r["frame"] == "threat"]
    hero_orig = [r for r in records if r["frame"] == "hero"]
    threat_turnout = sum(1 for r in threat_orig if r["persisted"]) / len(threat_orig)
    hero_turnout = sum(1 for r in hero_orig if r["persisted"]) / len(hero_orig)
    assert threat_turnout < hero_turnout

    summary = {
        "concept": "DataPersistenceBias",
        "tweet_turnout": round(stats["tweet_turnout"], 4),
        "author_turnout": round(stats["author_turnout"], 4),
        "mean_orientation_original": round(stats["mean_orig"], 4),
        "mean_orientation_recollected": round(stats["mean_rec"], 4),
        "orientation_shift": round(stats["orientation_shift"], 4),
        "threat_frame_turnout": round(threat_turnout, 4),
        "hero_frame_turnout": round(hero_turnout, 4),
        "verification": "passed",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
