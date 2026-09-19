# Security Policy & Threat Model Specification

**Project:** Sovereign Intent Architecture (SIA)  
**Document Status:** Formal Security & Vulnerability Policy (PoC / Grant Phase)  
**Target Standard:** Open Source Security Foundation (OSSF) & NLNet NGI Restack Hygiene Standards  

---

## 1. Threat Model & Architectural Boundaries

The Sovereign Intent Architecture (SIA) operates as an asynchronous, non-intrusive governance layer above legacy enterprise infrastructure. SIA is specifically engineered to mitigate **probabilistic boundary failures, hallucination drift, and unauthorized data exposure** inherent in Large Language Model (LLM) deployment.

+-------------------------------------------------+---------------------------------------------------+
|               OUT-OF-SCOPE                      |        IN-SCOPE: SIA DETERMINISTIC CAGE           |
|      (Physical Host / Kernel Security)          | (Prompt Injection / State Poisoning / Memory Leak)|
+-------------------------------------------------+---------------------------------------------------+
| * Malicious Hypervisor                          | * Adversarial Prompt Injection                    |
| * OS-Level Root Compromise                      | * Semantic Data Exposure ("Bundles of Risk")      |
| * Physical Hardware Tampering                   | * Model Logic Drift & Unchecked State Transitions |
|                                                 | * Transient Memory Residual Reconstruction        |
+-------------------------------------------------+---------------------------------------------------+

# 1.1 In-Scope Threat Mitigation Matrix

| Threat Vector | Attack Mechanism | SIA Layer Enforcement | Mitigation Primitive |
| :--- | :--- | :--- | :--- |
| **Adversarial Prompt Injection** | Cross-domain payload injection inside natural language context. | Layer 2 (FSM Cage) | Hard truncation via `SECURITY_VIOLATION_0x88` state transition (<15ms). |
| **Semantic Data Exposure** | Reconstructing PII from aggregated contextual logs. | Layer 2 (3-Tag Struct) | Semantic Decoupling (`[Entity]`, `[Factoid]`, `[State]`); zero raw text payloads in decision records. |
| **Transient Memory Reconstruction** | Cold-boot memory dumping or heap scanning of active SLM buffers. | Layer 2 (Memory Protocol) | C11 Just-In-Time zeroization via `memset_s()` clearing RAM to `0x00` immediately upon transaction exit. |
| **Unlawful Automated Decisioning** | Autonomous model execution bypassing human governance. | Layer 1 (Governance) | Non-Authorial AI Doctrine; models act strictly as linguistic parsers, FSM enforces human-authored invariants. |

### 1.2 Out-of-Scope Security Dependencies

SIA relies on the underlying Host Environment for the following security guarantees:
* **Host OS & Kernel Integrity:** Physical host hardening, Linux Kernel vulnerability patching, and OS access controls.
* **Network Enclave Isolation:** TLS 1.3 encryption for local edge IPC (Inter-Process Communication) channels.
* **Storage Encryption:** Hardware-level AES-256 encryption for underlying legacy datastores.

## 2. Responsible Vulnerability Disclosure

The SIA Core Engineering Team values security research from the open-source community. As an active Proof-of-Concept (PoC) research initiative under the NLNet NGI Restack framework, vulnerability reporting is governed by reasonable, best-effort operational parameters.

### 2.1 Disclosure Protocol

To report a suspected security flaw or FSM logic bypass:
* **Private Reporting Channel:** Do **NOT** open public GitHub issues for security vulnerabilities or exploit vectors.
* **Preferred Method:** Use GitHub's native **Private Vulnerability Reporting** feature directly within this repository. This guarantees encrypted end-to-end communication without exposing infrastructure maintainers.
* **Operational SLA:** Acknowledgment and initial triage are provided on a **best-effort basis**. As an open-source research PoC, fixed response or remediation timelines are explicitly disclaimed.

### 2.2 In-Scope Vulnerability Criteria

Reports are strictly prioritized for failures within the SIA Deterministic Cage:
1. **FSM Circuit Breaker Bypass:** Methods that bypass `SECURITY_VIOLATION_0x88` during active state drift.
2. **Memory Purge Incompleteness:** Failure of C11 `memset_s()` primitives to fully zeroize ephemeral RAM buffers on exit.
3. **3-Tag Hash Collisions:** Structural flaws in entity/factoid isolation leading to raw text leakage across domain boundaries.

---

## 3. Cryptographic Verification & Auditability

To maintain supply chain security and code integrity against tampering:
* **Commit & Tag Verification:** Official protocol releases and specification commits are cryptographically signed using GPG keys bound to repository maintainers.
* **Immutable State Audit:** Operational logs emit zero raw text payloads, consisting solely of deterministic SHA-256 state hashes and explicit FSM transition codes.

```bash
# Verify official release signatures
git tag -v v2.0.0-sia-core
```

## 4. Compliance Mapping & Legal Disclaimer

### 4.1 Regulatory Alignment Matrix

| Regulatory Framework | Article / Mandate | SIA Technical Compliance Mechanism |
| :--- | :--- | :--- |
| **EU AI Act** | Article 14 (Human Oversight) | Non-Authorial AI Governance; deterministic FSM overrides probabilistic SLM suggestions. |
| **EU AI Act** | Article 15 (Cybersecurity & Robustness) | Hard circuit breaking (`SECURITY_VIOLATION_0x88`) preventing logic drift and injection attacks. |
| **GDPR** | Article 17 (Right to Erasure / "To be Forgotten") | JIT transient RAM zeroization using C11 `memset_s()` primitives; zero residual storage. |
| **ISO 42001** | AI Management System (Traceability) | Auditability via immutable SHA-256 state hashes without raw text log exposure. |

### 4.2 Proof-of-Concept Disclaimer & Express Exclusion of Warranty

* **Research & Grant Scope:** This repository houses proof-of-concept specifications and prototype code developed under the NLNet NGI Restack research initiative. 
* **No Warranty:** THE SOFTWARE AND SPECIFICATIONS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. 
* **Operational Liability:** IN NO EVENT SHALL THE AUTHORS, ARCHITECTS, OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
