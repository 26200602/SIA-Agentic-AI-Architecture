# PoC: FSM-Verified Shadow Diagnostic Engine

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/26200602/my-colab-poc/blob/main/sia_fsm_boundary_sandbox.ipynb)

## Executive Summary

This Proof of Concept (PoC) serves as an **Executable Specification** for the **Shadow Diagnostic Engine** within the Sovereign Industrial Agentic (SIA) framework. It validates how unstructured operational jargon (e.g., informal chat messages from site supervisors or front-line staff) can be dynamically captured, interpreted by a Small Language Model (SLM), and mapped onto a deterministic Finite State Machine (FSM).

By utilizing **Transient Flushing** and **Zero-Knowledge Data Sovereignty**, this engine extracts structural operational telemetry and context latency without retaining sensitive raw text or introducing persistent privacy risks.

---

## Architectural Workflow

The diagram below illustrates the end-to-end data pipeline from raw message ingestion to FSM verification and immutable audit logging:

```mermaid
flowchart TD
    A[Front-line Communication Ingestion\nWhatsApp / Teams Jargon] -->|@mention Trigger| B[Ephemeral SLM Ingestion Layer]
    B -->|Context Analysis| C[FSM State Alignment Engine]
    
    subgraph Data Sovereignty Boundary
        B -.->|Transient Flushing\nImmediate Raw Text Purge| D[(Zero-Knowledge Memory Buffer)]
    end
    
    C -->|Map to FSM ID| E[Decision Packet Generator]
    E -->|Structured Output| F[Audit Trail / Enterprise Ledger]
    
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px
    style E fill:#bfb,stroke:#333,stroke-width:2px
```

# Front-Line Conversational Streams Integration PoC

This repository contains the Proof of Concept (PoC) directory housing the core data contracts and telemetry schemas used to integrate front-line conversational streams into enterprise governance platforms.

## 📄 Artifacts & Specifications

* **`decision-packet.schema.json`**
  * **Purpose:** JSON Schema (Draft-07) defining the strict data contract for Finite State Machine (FSM) decision packets.
  * **Key Attributes:** Enforces structured typing for `fsm_state_id`, `context_latency`, and `data_sovereignty` verification flags.

* **`mock-telemetry-event.json`**
  * **Purpose:** A real-world instance demonstrating the transformation of informal Cantonese site jargon (*跟口頭指示做住先*) into a validated FSM override code (`FSM_ERR_OVERRIDE_001`).

* **`sia_fsm_boundary_sandbox.ipynb`**
  * **Purpose:** Interactive Google Colab Sandbox for testing FSM boundary logic and Small Language Model (SLM) translation accuracy using open-access models.
  * **Link:** [Open in Google Colab](https://colab.research.google.com/github/) *(Replace with your actual notebook URL)*

## 🚀 Execution Guide for Technical Teams

Follow these steps to validate this PoC in a local or cloud environment:

### 1. Sandbox Interactive Testing
* Click the **Open in Colab** badge at the top of the repository to launch the notebook.
* Run the cells sequentially using free **GPU / T4 runtime resources** to observe real-time state extraction.

### 2. Schema Verification
* Use standard JSON Schema tools to validate downstream payloads against `decision-packet.schema.json`.
* **Example via Python:**
  ```python
  import json
  from jsonschema import validate

  # Load your schema and instance
  with open("decision-packet.schema.json") as s:
      schema = json.load(s)
  with open("mock-telemetry-event.json") as i:
      instance = json.load(i)

  # Validate
  validate(instance=instance, schema=schema)
  print("Validation successful!")
  ```
* **Example via CLI:**
  ```bash
  jsonschema -i mock-telemetry-event.json decision-packet.schema.json
  ```
# Example validation using Python jsonschema CLI
jsonschema -i mock-telemetry-event.json decision-packet.schema.json

** This document was structured with the help of AI, and curated by Sana.M ***
