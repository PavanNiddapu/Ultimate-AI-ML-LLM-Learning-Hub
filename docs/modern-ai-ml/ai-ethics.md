# AI Ethics and Responsible AI

Objective: Build systems that are fair, accountable, privacy-preserving, and transparent, with governance that scales.

Key Concepts:
- Framing harms: allocative vs. representational; individual vs. group
- Fairness: definitions (equalized odds, demographic parity, calibration), tradeoffs
- Privacy: differential privacy, k-anonymity, PII handling, synthetic data
- Transparency: model and data cards, system cards, disclosures
- Accountability: decision logs, appeal mechanisms, incident response
- Governance: risk tiers, approval workflows, evaluations, documentation
- Evaluations: pre-deployment (offline), pre-launch (red teaming), post-deployment monitoring

Hands-on:
1) Build a bias evaluation notebook:
   - Compute group fairness metrics on a held-out dataset
   - Render a report with AUC, TPR/FPR by subgroup, and parity gaps
   - Add thresholds and fail the CI if gaps exceed policy limits
2) Add a privacy layer:
   - Train simple models with DP-SGD (Opacus or TF Privacy) and compare utility
   - Explore data minimization and PII scanners in the data ingest step
3) Documentation:
   - Create a Model Card and Data Card templates for your project
   - Include risk assessment and intended-use/out-of-scope sections

Templates:
- model_card.md: purpose, training data, metrics (including subgroups), risks, mitigations, updates
- data_card.md: provenance, licenses, known biases, consent, processing, retention

Resources:
- Fairlearn, AIF360
- Privacy: Opacus, TensorFlow Privacy; DP reading lists
- Documentation: Model Cards (Mitchell et al.), Datasheets for Datasets (Gebru et al.)
- Governance: NIST AI RMF, ISO/IEC 42001 (AI management system), EU AI Act overviews