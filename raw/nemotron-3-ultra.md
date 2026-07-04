# NVIDIA Nemotron 3 Ultra

Source: https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/
Published: June 04, 2026

We present our most capable model yet – Nemotron 3 Ultra with 550 billion
total and 55 billion active parameters. Nemotron 3 Ultra is the final and
best model of the Nemotron 3 family of models.

## Key Features
- Employs Mixture-of-Experts Hybrid Mamba-Attention architecture.
- Leverages LatentMoE for improved accuracy.
- Includes MTP layers for faster inference through native speculative decoding.
- Supports inference time reasoning budget control.
- Pretrained in NVFP4.
- Post-trained with enhanced pipeline involving Supervised Fine Tuning (SFT),
  Reinforcement Learning (RL), and Multi-teacher On-Policy Distillation (MOPD)
  for improved model accuracy.

## Key Highlights
- Nemotron 3 Ultra achieves 5.9x, 4.8x, and 1.6x higher inference throughput
  compared to GLM-5.1-754B-A40B, Kimi-K2.6-1T-A32B, and Qwen-3.5-397B-17B
  respectively on the 8k token input / 64k token output setting.
- Nemotron 3 Ultra achieves on-par accuracies compared to other
  state-of-the-art open LLMs across a diverse set of benchmarks.
- Supports context length of up to 1M tokens while outperforming
  state-of-the-art open LLMs on RULER at 1M context length.

## Open Source
We are releasing the pre-trained, post-trained, and quantized checkpoints
along with the datasets used for training.

### Checkpoints
- Nemotron 3 Ultra 550B-A55B NVFP4: post-trained and NVFP4 quantized model
- Nemotron 3 Ultra 550B-A55B BF16: post-trained model
- Nemotron 3 Ultra 550B-A55B Base BF16: base model
- Nemotron 3 Ultra 550B-A55B GenRM: GenRM used for RLHF

### Data
- Nemotron-Pretraining-Code-v3: 173B tokens of fresh code data from GitHub
  through September 30, 2025.
- Nemotron-Pretraining-Legal-v1: A collection of synthetic datasets intended
  to improve the legal capabilities of LLMs.
- Nemotron-Pretraining-Specialized-v1.2: A collection of synthetic datasets
  aimed to improve LLM capabilities on factual recall, moral scenarios, and
  diverse generative and multiple choice questions.
- Nemotron-Posttraining-v3: A collection of post-training datasets for
  improving agentic, reasoning, and general model capabilities during SFT
  and RL.

## Links
- Models (Hugging Face collection): https://huggingface.co/collections/nvidia/nvidia-nemotron-v3
- Tech Report (PDF): https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf
- Nemotron 3 Blog: https://research.nvidia.com/labs/nemotron/Nemotron-3/
