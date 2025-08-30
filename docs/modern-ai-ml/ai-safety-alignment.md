# AI Safety and Alignment

Objective: Understand risk taxonomies, red teaming, evaluations, and mitigations for capable AI systems.

Scope:
- Safety vs. security vs. ethics: relationships and boundaries
- Capability-specific risks: hallucination, jailbreaks, prompt injection, data exfiltration
- Harm classes: misinformation, harmful instructions, privacy leaks, IP violations
- Alignment strategies: instruction tuning, RLHF/RLAIF, constitutional constraints, tool-use restrictions
- Evaluation strategies: adversarial testing, structured evals, model spec conformance checks
- Operational safety: rate limits, abuse prevention, human-in-the-loop escalation

Hands-on:
1) Build an evaluation harness:
   - Define scenarios and attack vectors (prompt injection, jailbreaks, data extraction)
   - Add automatic scoring for refusal/containment and leakage
   - Log failures with traces and seeds for reproducibility
2) Red teaming workflow:
   - Pair adversarial prompts with expected behaviors
   - Triage, categorize, and prioritize fixes
3) Mitigations:
   - Safety policies and rule-based guards
   - Classifiers and rejection heads
   - Prompt engineering patterns (sandwich, system messages, tool-use boundaries)
   - Retrieval and tool sandboxing; output filtering; watermark policies

Governance:
- Model/system cards with safety sections and known limitations
- Launch gates: pass/fail thresholds across safety eval suites
- Incident management: detection, response, communication, postmortem, model updates

Resources:
- Eval frameworks: HELM-style evals, OpenAI Evals, Robust Intelligence, MLCommons
- Safety papers and industry frameworks: NIST GenAI, UK AI Safety Summit materials
- Red teaming best practices and taxonomies