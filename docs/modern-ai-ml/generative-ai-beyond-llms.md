# Generative AI Beyond LLMs

Objective: Learn generative techniques for images, audio, video, and structured data beyond text-only LLMs.

Model Families:
- Diffusion models: DDPM, DDIM, Latent Diffusion (Stable Diffusion), ControlNet, LoRA fine-tuning
- VAEs and VQ-VAEs: discrete latents for images/audio
- GANs: still relevant for certain modalities and high-fidelity synthesis
- Multimodal models: text-to-image, image-to-image, text-to-audio, image-conditioned video
- Audio: diffusion and autoregressive TTS, music generation, vocoders (HiFi-GAN)
- Video: latent video diffusion, consistency models

Hands-on tracks:
Track A: Image generation
1) Run Stable Diffusion with a small LoRA fine-tune on a domain dataset
2) Add ControlNet for edge/pose guidance
3) Export a lightweight pipeline with FP16 and attention optimizations

Track B: Audio/TTS
1) Build a text-to-speech pipeline using open models
2) Evaluate intelligibility (WER) and naturalness (MOS-like human rating)
3) Add content safety filters and watermark checks where applicable

Track C: Multimodal
1) Use CLIP to score prompt-image alignment
2) Build a retrieval-augmented image generator that selects references
3) Evaluate alignment and diversity metrics (FID, CLIPScore, Inception Score caveats)

Operational concerns:
- Content safety: NSFW, copyright, watermarking and provenance (C2PA)
- Dataset licenses and attribution; consent and opt-outs
- Prompt injection and misuse monitoring for hosted generators

Resources:
- Diffusers (Hugging Face), CompVis Stable Diffusion, ControlNet
- Audio: TTS models (e.g., Coqui, Bark), vocoders, audiocraft repos
- Metrics: FID, KID, CLIPScore; cautions on metric reliability