# Shadow Diagnostic Engine (Field Operations Reference Case)

> **SIA Pillar 2 Reference Implementation**: Non-Intrusive Event Shadowing & Anti-Surveillance Gatekeeping for Cross-Enterprise Operations.
> 
**Core Repositories & Execution Anchors**: 

* 📄 **Anonymizer & Context Parser Layer**: [anonymizer_and_parser.py](./src/anonymizer_and_parser.py)
* 📊 **Mock Project System Logs**: [mock_project_logs.json](./src/mock_project_logs.json)
* 📐 **Core Architecture Blueprint**: [README.md](./README.md)

---

## Executive Summary

Enterprise field operations (construction, maritime, and large-scale engineering) are chronically bottlenecked by "Legacy Data Debt" and communication friction across multiple external stakeholders (Asset Owners, EPCs, Sub-contractors). Traditional generative AI solutions fail in these environments because they demand invasive ambient monitoring, violate cross-enterprise privacy boundaries, and introduce probabilistic hallucinations into safety-critical workflows.

The **Shadow Diagnostic Engine** implements SIA Pillar 2 (Non-Intrusive Implementation & Boundary Isolation). It operates as a read-only, event-driven gateway that intercepts unstructured frontline communications, extracts discrete "Factoids" via localized SLMs, and enforces hard safety limits using a deterministic Finite State Machine (FSM) circuit breaker—ensuring zero raw data egress and absolute auditability.

---

## Architectural Topology

```mermaid
graph TD
    subgraph Ingestion ["Frontline Channel Shadowing (Non-Intrusive)"]
        A[Frontline Channels: WhatsApp / Voice / Chat] -->|Unstructured Stream| B[Read-Only Ingestion Buffer]
    end

    subgraph Execution ["Sovereign Edge Node (T4 / Local NPU)"]
        B --> C[Ephemeral Parser: Local SLM]
        C -->|3-Tag Extraction: Entity, Factoid, State| D{Deterministic FSM Engine}
        
        D -->|Violation: Out-of-Boundary| E[Circuit Breaker Intercept\nSECURITY_VIOLATION_0x88]
        
        D -->|Valid Transition| F[Transient Factoid Payload]
        F --> G[Cryptographic Hash Logger]
        G --> H[Memory Purge: memset_s]
    end

    subgraph Immutable ["Enterprise Core"]
        G -->|SHA-256 Audit Hash| I[(Immutable Ledger / ERP)]
    end

    classDef danger fill:#ffdddd,stroke:#990000,stroke-width:2px,color:#990000;
    classDef success fill:#ddffdd,stroke:#009900,stroke-width:2px,color:#006600;
    class E danger;
    class H success;
```

---

## Strategic Mechanics & Operational Pillars

### 1. Anti-Surveillance & Event-Driven Activation
Unlike consumer-grade AI agents that demand full-desktop keylogging or persistent video streams, the Shadow Diagnostic Engine is strictly **Event-Driven and On-Demand**.
* **Zero Ambient Surveillance:** The engine does not record ambient audio, track idle screen time, or inspect private personal traffic.
* **Bounded Interception:** Processing is triggered only when specific operational risk vectors or system keywords (e.g., `Material Substitution`, `Structural Modification`, `Safety Boundary`) are detected in the communication buffer.
* **Privacy Boundary:** Irrelevant dialogue is instantly discarded at the memory buffer stage prior to semantic evaluation.

### 2. Cross-Enterprise Boundary Isolation (Internal vs. External)
Field operations inherently span multiple legal entities: Asset Owners, EPC Contractors, and Sub-Contractors. 
* **Zero Client Footprint:** External vendors interact via their native communication tools. No corporate MDM (Mobile Device Management) or proprietary app installation is forced onto third-party devices.
* **Logical Segregation via 3-Tag Logic:** Incoming unstructured site data is parsed into three isolated tags:
  1. `[Entity_ID]` (Pseudonymized Vendor/Site Identifier)
  2. `[Metric_Factoid]` (e.g., Rebar Gauge changed from 300mm to 400mm)
  3. `[State_Context]` (Current Project Stage)
* Identity is strictly decoupled from operational payload before any cross-boundary analysis occurs.

### 3. Non-Intrusive Legacy Shadowing
The engine operates strictly as a **Read-Only Shadow Layer** on top of existing communication systems and legacy ERPs.
* **Zero Schema Mutation:** Production databases and legacy project management systems remain untouched.
* **Asynchronous Triplet Formation:** Unstructured voice notes and chat images are converted into subject-predicate-object triplets in memory without locking production tables.

### 4. Deterministic FSM Gatekeeping & Memory Zeroization
To eliminate model hallucination in safety-critical operations, execution logic is enforced by a hard deterministic state machine.
* **Circuit Breaker Intercept:** If a field decision violates predefined structural safety parameters or regulatory thresholds, the FSM instantly trips a circuit breaker, halts automated propagation, and flags an explicit exception.
* **Zero-Trace Ephemeral Processing:** Upon transaction finalization, raw chat payloads and intermediate SLM reasoning states are purged from RAM using `memset_s` equivalents. Only a **SHA-256 Immutable State Hash** is retained for audit logging.

---

## Repository Structure & Verification Anchors

```text
shadow-diagnostic-engine/
├── README.md                           # Architecture Specification (This File)
├── fsm_policy.json                     # Declarative State Boundary & Circuit Breaker Rules
└── sim_poc.py                          # Deterministic FSM Interceptor Executable
```

### Declarative Policy Logic (fsm_policy.json)
```json
{
  "DOMAIN": "FIELD_OPERATIONS_CONSTRUCTION",
  "STATES": ["SITE_INSPECTION", "CHANGE_REQUEST", "COMPLIANCE_VERIFIED", "REJECTED_HALT"],
  "ALLOWED_TRANSITIONS": {
    "SITE_INSPECTION": ["CHANGE_REQUEST"],
    "CHANGE_REQUEST": ["COMPLIANCE_VERIFIED", "REJECTED_HALT"]
  },
  "MANDATORY_FACTOIDS": ["SPEC_METRIC", "SAFETY_IMPACT", "AUTHORIZATION_LEVEL"],
  "CIRCUIT_BREAKER_RULES": {
    "UNAUTHORIZED_SPEC_CHANGE": {
      "TRIGGER": "SAFETY_IMPACT == 'HIGH' AND AUTHORIZATION_LEVEL < 3",
      "ACTION": "TRIP_CIRCUIT_BREAKER",
      "EXIT_CODE": "SECURITY_VIOLATION_0x88"
    }
  }
}
```
## Verification & Deployment Strategy

### Local Edge Execution
The lightweight SLM parsing layer runs on localized edge hardware (e.g., T4 GPU or local NPU) to minimize latency (<20ms) and prevent raw data egress to external public clouds.

### Audit Verification

To evaluate how the FSM interceptor halts out-of-boundary site modification requests in real time using deterministic rule enforcement, execute the sovereign audit script located in the repository:

```bash
python use-cases/shadow-diagnostic-engine/src/anonymizer_and_parser.py
```


### NLNet Open Standard Alignment
Designed in compliance with NGI (Next Generation Internet) European Digital Sovereignty standards, ensuring non-authorial AI governance, full auditability, and absolute user privacy preservation.


