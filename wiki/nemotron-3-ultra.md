---
title: NVIDIA Nemotron 3 Ultra
type: source
date: 2026-07-04
sources: 2
tags: [llm, moe, mamba, nvidia, model-release, quantization, inference]
source_url: https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/
captured: 2026-07-04
version: published 2026-06-04 (landing page); tech report dated 2026-06-09
---

Largest and most capable model in NVIDIA's Nemotron 3 family: 550B total / 55B
active parameter Mixture-of-Experts Hybrid Mamba-Attention model, positioned
for long-running agentic tasks. Full tech report: "Nemotron 3 Ultra: Open,
Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic
Reasoning."

## Architecture
- Hybrid Mamba-2 / Attention backbone (same layer pattern as Nemotron 3 Super,
  scaled to 550B/55B): 108 total layers, model dim 8192, 64 Q-heads / 2 KV-heads,
  512 experts/layer with top-22 routed, MoE latent size 2048.
- **[[latentmoe]]** for MoE layers — trades hidden-dimension width for more
  routed experts at fixed inference cost, improving accuracy per active
  parameter over standard granular MoE.
- Native **Multi-Token Prediction (MTP)**, 2 shared-weight heads, used both for
  training regularization and inference-time speculative decoding (draft length
  6 gives best speedup: 2.89x over no-MTP baseline on a 10K/16K/BS=1 workload).
- Reasoning-effort control: inference-time accuracy/compute trade-off knob.

## Pretraining
- 20T text tokens, NVFP4 precision throughout (largest-scale stable NVFP4
  pretraining demonstrated to date; final 15% of layers, MTP layers, and
  embeddings kept in higher precision).
- Two-phase Warmup-Stable-Decay schedule: phase 1 (15T tokens) biased toward
  diversity, phase 2 (5T tokens) biased toward quality.
- New pretraining data released: `Nemotron-Pretraining-Code-v3` (173B code
  tokens through Sept 2025), `Nemotron-Pretraining-Legal-v1` (boosted a proxy
  LegalBench average from 64.6 to 74.7 in ablation), `Nemotron-Pretraining-Specialized-v1.2`.
- Long-context extension: continuous pretraining to 1M tokens (92% of
  iterations at 1M, 8% at 4K to preserve short-benchmark accuracy), 33B tokens
  total, no RULER-style data in the blend yet still leads RULER @ 1M.

## Post-training
Base -> SFT -> RLVR -> **[[multi-teacher-on-policy-distillation]]** (2
iterations) -> MTP boosting -> Nemotron 3 Ultra. Redesigned from the Nemotron 3
Super pipeline specifically to add MOPD as a second capability-acquisition
lever alongside RL.

- **SFT**: two-stage (294K then 515K token packed sequences), broad data mix
  (long-context, safety incl. 6-language translated safety blend, search
  incl. OpenResearcher subset, terminal-use ~370K trajectories, SWE issue
  resolution with heuristic trajectory filtering, math/proof, CUDA kernel
  generation, RTL, multilingual).
- **RLVR**: unified GRPO-style training across agentic/reasoning/safety/chat
  environments simultaneously, batch size 8192, 16 rollouts/sample.
- **MOPD**: see [[multi-teacher-on-policy-distillation]] for the mechanism.
  10+ specialized teachers (SWE, office/GDPval, search, terminal-use,
  conversational tool-use, model usability, agentic safety, chat/GenRM,
  instruction-following/factuality, STEM). Recovery rates (fraction of
  teacher-student gap closed) ranged from 16.9% (HLE) to 172.7% (Terminal
  Bench 2.0, i.e. surpassed the teacher) — MOPD works best when the teacher's
  advantage is expressible as token-level trajectory preferences the student
  can already sample; weakest on self-contained reasoning (HLE) where the
  teacher's edge comes from off-policy SFT/RL data the student never saw.

## Quantization
Post-training quantization to NVFP4 for Blackwell inference. Swept
bits-per-element from 4.85 to 7.19; selected **5.03 BPE** (NVFP4 + mixed FP8)
as the smallest budget with no measurable accuracy loss — everything but
long-context reasoning (AA-LCR) saturates even at 4.85 BPE, and AA-LCR
recovers fully at 5.03 via the mixed-FP8 layers. Weight scale selection uses
"Four-Over-Six" (choosing per-block between M=4/M=6 FP4 grids), which won for
routed experts at the 5.03 operating point despite MSE calibration reducing
raw weight-MSE further — no consistent accuracy gain from that extra MSE
reduction.

## Inference
- Prefill is compute-bound (FLOPs ~ active params) so Ultra trails
  smaller-active-param models like Qwen-3.5-397B-17B on prefill-heavy
  workloads; decode is I/O-bound (bandwidth ~ total params + Mamba's
  constant-per-step state cost) so Ultra leads decode-heavy workloads (1.6x
  over Qwen-3.5 at 8K/64K).
  - Reported throughput vs. GLM-5.1-754B-A40B / Kimi-K2.6-1T-A32B /
    Qwen-3.5-397B-17B: 5.9x / 4.8x / 1.6x respectively (8K in / 64K out, NVFP4, GB200).
- Wide expert parallelism (EP) wins at high-throughput/large-batch (all-to-all
  bound, no AllReduce on critical path); wide tensor parallelism (TP) wins at
  low-latency/small-batch (weight-read bound). GB200 NVL72's single NVLink
  domain suits both.
- Prefill-decode disaggregation adopted; required upstreaming hybrid
  Mamba-Attention KV-cache/SSM-state transfer support in vLLM (~10% throughput
  gain on prefill-heavy workloads).
- Adopted FlashInfer NVLinkOneSided all-to-all backend over default vLLM
  AllGather+ReduceScatter (~5% throughput gain); MoE-side chunking landed
  upstream to fix wide-EP prefill chunking limits.

## Checkpoints & data (open-sourced on Hugging Face)
- Checkpoints: `Nemotron 3 Ultra 550B-A55B NVFP4` (quantized), `...BF16`
  (post-trained), `...Base BF16`, `...GenRM`.
- Datasets: `Nemotron-Pretraining-Code-v3`, `Nemotron-Pretraining-Legal-v1`,
  `Nemotron-Pretraining-Specialized-v1.2`, `Nemotron-Posttraining-v3`.
- Models collection: https://huggingface.co/collections/nvidia/nvidia-nemotron-v3
- Recipes/code: https://github.com/NVIDIA-NeMo/Nemotron
- Tech report: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf

## Open problems noted in the report
- MOPD via full-distribution/logit matching underperformed the sampled-token
  objective — teacher logits on student-generated, off-teacher-support prefixes
  are poorly calibrated.
- No systematic study yet of unifying teacher/student SFT before specialization
  to avoid the distribution-mismatch problem MOPD warmup patches over.
- End-to-end long-horizon agentic rollouts in MOPD remain inefficient
  (mixing multi-turn agentic with single-turn reasoning environments causes
  rollout-time imbalance); current workaround is single-turn rollouts
  (PivotRL-style) for most agentic tasks.
