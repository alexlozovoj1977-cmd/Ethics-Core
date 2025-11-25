# Changelog – Ethics-Core ECP Extension

All notable changes to this project will be documented in this file.

The format is inspired by Keep a Changelog and semantic versioning, adapted to the
research/prototype nature of Ethics-Core.

---

## [1.5.0] – 2025-11-25 – ECP Extension (Local Cognitive Parity)

### Added
- Defined **Local Ethical Cognitive Parity** as:
  - Ethics-Core v1.4.2 +
  - Φ6 (Symmetric Access & Auditability) +
  - Φ7 (Prioritized Vulnerability) +
  - Φ8 (Epistemic Humility) +
  - Co-Think Mode +
  - ECP Integrity Check.
- Introduced core spec:
  - `ETHICS_CORE_v2.0_ECP_DRAFT.md` (normative draft for v2.0).
- Added operational protocol:
  - `ECP_PROTOCOL_v1.5.md` for Co-Think Mode.
- Implemented minimal integrity logic:
  - `ecp_integrity_check.py` with states ECP_ACTIVE, ECP_UNCERTAIN, ECP_IMPOSSIBLE.
- Added test scenarios:
  - `ecp_scenarios.jsonl` covering key combinations of Φ6–Φ8 and infra constraints.
- Added governance workflow:
  - `ecp_approval_workflow.md` for ECP activation, monitoring and suspension.
- Updated documentation:
  - `README.md` to reflect ECP Extension and repository layout.

### Notes
- This is a **research-grade** release, not a production safety guarantee.
- Systemic (global) ECP remains out of scope; this version focuses on
  **local parity** between a single human Primary Agent and a single AI core.

---

## [1.4.2] – Pre-ECP Ethics-Core

- Baseline Ethics-Core with:
  - Truth-First, Non-Harm, No-Coercion.
  - Reproducibility and Multi-Layer Evaluation.
  - AAR and red lines.
- Served as the foundation for the ECP Extension in v1.5.0.
