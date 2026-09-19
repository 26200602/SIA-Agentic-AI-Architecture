# Contributing Guidelines & Governance Protocol

**Project:** Sovereign Intent Architecture (SIA)  
**Status:** Open-Source Policy Specification & Core Engineering Standard  
**Compliance Target:** NLNet NGI Restack & EU AI Act (Article 14 Human Oversight)  

---

## 1. Architectural Principles & Non-Authorial AI Doctrine

All contributions to the Sovereign Intent Architecture (SIA) repository must adhere to strict deterministic boundaries and non-authorial governance:

* **Human-in-the-Loop Authority:** In compliance with EU AI Act Article 14, generative AI models act strictly as linguistic parsers and formatting engines. Core execution state machines, memory abstractions, and circuit breakers must originate from explicit human engineering.
* **Deterministic Isolation:** No contribution will be accepted that introduces probabilistic output directly into decision-critical memory layers without an intervening Finite State Machine (FSM) cage.

---

## 2. Pull Request (PR) & Code Review Standards

To maintain software supply chain safety, code contributions must pass human architectural review prior to merging into `main`.

### 2.1 Acceptance Criteria (Quality Gates)

Any Pull Request modifying Layer 1/2 specifications, C/Rust primitives, or state machine execution logic must satisfy the following invariants:

1. **FSM Interception Latency:** State drift or cross-domain injection triggers must deterministically transition to `SECURITY_VIOLATION_0x88` within **$< 15\text{ms}$**.
2. **Zero Residual Memory:** Code exiting a transaction context must execute JIT memory zeroization via C11 `memset_s()` primitives. Hard-coded or compiler-optimized transient memory retainers are grounds for immediate PR rejection.
3. **Decoupled Data Flow:** Direct text-payload pass-through into legacy datastores is forbidden. All inputs must map to the ephemeral 3-Tag structure (`[Entity]`, `[Factoid]`, `[State]`).

### 2.2 Commit Verification (Recommended)

To protect the software supply chain against unauthorized commits:
* Repository maintainers and contributors are strongly encouraged to sign commits using GPG or SSH keys verified by GitHub.
* Unsigned commits undergoing critical architectural changes will face secondary manual review by the lead architect.

---

## 3. Governance & Maintainer Contact

* **Lead Maintainer & Architect:** Sovereign Intent Architecture Engineering Group
* **Scope:** Proof-of-Concept (PoC) Research & Grant Due Diligence Phase under NLNet NGI Restack.
