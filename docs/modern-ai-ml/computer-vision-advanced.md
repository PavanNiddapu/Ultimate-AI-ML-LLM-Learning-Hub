# Computer Vision (Advanced)

Objective: Go beyond classification into detection, segmentation, tracking, multi-modal, and efficiency techniques for production CV.

Key Topics:
- Detection: Faster/Mask R-CNN, YOLOv7/8, DETR and variants
- Segmentation: semantic vs. instance vs. panoptic; Segment Anything (SAM)
- Tracking and video: SORT/DeepSORT, ByteTrack, tracking-by-detection vs. joint models
- 3D: monocular depth, NeRFs, SLAM basics
- Multimodal: CLIP, BLIP-2, LLaVA, grounding with SAM/OWL-ViT
- Efficiency: pruning, quantization (PTQ/QAT), distillation, TensorRT/ONNX Runtime
- Data-centric CV: active learning, synthetic data, augmentation policies (RandAugment, AutoAugment)

Hands-on:
1) Train or fine-tune a detector (YOLOv8 or DETR) on a small custom dataset
2) Export to ONNX/TensorRT; compare throughput/latency on CPU vs GPU
3) Integrate SAM for interactive segmentation; optional: add a WebUI
4) Add tracking to a video pipeline and evaluate MOTA/MOTP
5) Evaluate robustness: corruptions (ImageNet-C style), lighting changes, and occlusions

Evaluation:
- mAP, IoU, PQ (panoptic), throughput (fps), latency (p50/p95), accuracy-robustness tradeoffs
- Edge constraints: memory, compute, power; model size vs. performance

Resources:
- Ultralytics YOLO, DETR implementations, Segment Anything, ONNX Runtime/TensorRT
- Papers: DETR, SAM, RT-DETR, Grounding DINO, EfficientNetV2