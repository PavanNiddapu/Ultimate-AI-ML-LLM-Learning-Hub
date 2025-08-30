# MLOps and Model Deployment

Objective: Learn how to reliably build, deploy, monitor, and iterate on ML systems in production.

Prerequisites:
- Comfortable with Python, containers (Docker), and basic cloud concepts
- Familiarity with training ML models locally

Key Concepts:
- System boundaries: data pipelines, training jobs, model registry, deployment targets, inference fleet
- Environments and reproducibility: containers, pinned deps, hermetic builds
- CI/CD for ML: training pipelines vs. app pipelines, gated promotions, canaries
- Experiment tracking and model registry: MLflow, Weights & Biases, SageMaker, Vertex AI
- Serving options:
  - Batch vs. online vs. streaming
  - Serverless (Cloud Run, Lambda), managed endpoints (SageMaker/Vertex), K8s (KServe/Seldon)
  - Vector DBs and feature stores (Feast, Tecton)
- Observability:
  - Model performance: drift, data quality, performance regressions
  - Application performance: p95 latency, error budgets (SLOs)
  - ML-specific monitoring: feature distributions, label delay, bias metrics
- Governance:
  - Versioning: data, code, models, infra-as-code (IaC)
  - Reproducibility: pipelines + artifact lineage (OpenLineage)
  - Approvals: automated checks + human-in-the-loop signoff

Hands-on (choose one path):
Path A: OSS stack on local/K8s
1) Build a FastAPI inference service that loads a model from MLflow registry
2) Containerize with Docker; include health/readiness probes
3) Write a GitHub Action to:
   - Run tests + type checks
   - Build and push image
   - Deploy to a K8s namespace via Kustomize/Helm
4) Add Prometheus metrics (latency, throughput) and a basic Grafana dashboard
5) Add drift detection with Evidently or whylogs on sampled traffic
6) Canary rollout: progressive traffic shifting with Argo Rollouts

Path B: Managed cloud
1) Train in Vertex AI or SageMaker with experiment tracking
2) Register the model in the managed registry
3) Deploy to a serverless endpoint with autoscaling
4) Configure monitoring for skew, drift, and prediction distribution

Checklists:
- Pre-deploy: unit+integration tests, security scan, reproducible build, data contracts
- Post-deploy: SLOs defined, alerts wired, rollback plan, shadow/canary tested
- Compliance: model card, dataset card, approvals recorded, audit trail

Resources:
- MLflow, KServe, Seldon, BentoML
- Orchestration: Airflow, Dagster, Prefect
- Monitoring: Evidently, Arize, Fiddler, whylogs
- Papers/Guides: Hidden Technical Debt in ML Systems; Google's MLOps whitepapers; Microsoft MLOps maturity model