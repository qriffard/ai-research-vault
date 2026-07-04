---
title: Multi-teacher On-Policy Distillation (MOPD)
type: concept
date: 2026-07-04
sources: 1
tags: [post-training, distillation, rl, llm]
---

Post-training technique that trains a single student model against many
domain-specialized teacher models simultaneously, using dense token-level
KL supervision on the student's *own* rollouts rather than sparse
environment reward. Introduced in this form in [[nemotron-3-ultra]]'s tech
report (building on prior on-policy distillation work: Yang et al. 2026,
Lu & Lab 2025, Xiao et al. 2026).

## Why it exists
Mixed-environment RLVR (single policy trained across all domains at once)
dilutes the per-domain learning signal as the number of environments grows —
each domain gets only a thin slice of every training batch. MOPD's fix:
train 10+ narrow specialist teachers first (each with its own SFT/RL recipe),
then distill all of them into one student.

## Mechanism
- Student generates rollouts across all domains; each rollout gets scored by
  its matching domain teacher.
- Objective is negative reverse-KL between student and teacher distributions,
  evaluated only at states the *student* actually visits (sampled-token
  objective) — not full-distribution/logit matching, which underperformed in
  ablations because teacher logits are poorly calibrated off the teacher's
  own support.
- Run asynchronously (rollout generation / teacher scoring / student
  optimization pipelined), with a proximal-policy decoupling to handle
  stale rollouts from lagging workers.
- Iterative: after one MOPD round, branch new teachers from the updated
  student and merge back in a second round. Nemotron 3 Ultra used 2 iterations.

## The distribution-mismatch problem
If teacher and student were trained on divergent SFT data, student rollouts
land outside the teacher's support and supervision quality degrades. Fix is a
lightweight "MOPD warmup": brief SFT on data drawn from the teacher's own
distribution before distillation, to pull student rollouts back into the
teacher's support. Warmup helped agentic benchmarks substantially (e.g. GDPVal
28.9 -> 46.7) but did almost nothing for self-contained reasoning (HLE) —
there the gap comes from off-policy SFT/RL data the teacher saw and the
student didn't, not from a shallow trajectory mismatch warmup can fix.

## Open problems
- Full-distribution/logit-matching variants of the objective underperform
  sampled-token — unresolved when broader distributional supervision would help.
- No systematic comparison yet of "unify SFT before specializing teachers" vs.
  today's parallel-development approach.
- Long-horizon agentic rollouts (many turns) mixed with single-turn reasoning
  environments cause severe rollout-time imbalance in the async pipeline;
  current workaround is restricting to single-turn rollouts for agentic tasks.

See [[nemotron-3-ultra]] for the full results table (recovery rates by domain).
