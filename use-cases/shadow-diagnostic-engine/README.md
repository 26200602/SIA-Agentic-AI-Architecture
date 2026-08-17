# Use Case: Shadow Diagnostic Engine

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/26200602/SIA-Agentic-AI-Architecture/blob/main/use-cases/shadow-diagnostic-engine/poc/sia_fsm_boundary_sandbox.ipynb)

## Executive Summary

The **Shadow Diagnostic Engine** addresses a critical challenge in enterprise AI adoption: capturing non-standard, front-line operational knowledge ("shadow workflows") without compromising enterprise data governance or introducing model non-determinism.

### Problem Statement
Front-line personnel frequently rely on informal domain heuristics expressed in local vernacular (e.g., operational Cantonese jargon). Traditional AI deployments either fail to map these unscripted inputs accurately or risk compliance breaches when raw conversational inputs pass unvetted into core systems.

### Architectural Solution
Under the **SIA Framework**, the Shadow Diagnostic Engine enforces a decoupled, zero-trust boundary architecture:
* **Ephemeral SLM Mapping:** Translates unstructured front-line jargon into deterministic Finite State Machine (FSM) state codes.
* **Zero-Knowledge Data Sovereignty:** Executes immediate transient memory flushing (`raw_text_retained = False`) post-translation.
* **Strict Schema Governance:** Enforces Draft-07 JSON Schema validation before any decision packet is transmitted downstream.

## System Architecture & Data Flow

```mermaid
graph TD
    A[Front-Line Operator Input] -->|Cantonese Jargon| B[Ephemeral SLM Engine]
    B -->|Semantic Alignment| C[FSM State Code Allocation]
    C -->|Construct Packet| D[JSON Schema Validator]
    
    subgraph Data Sovereignty Boundary
        B -.->|Transient Flushing| E[(Memory Purged)]
        E -.->|raw_text_retained: False| F[Zero-Knowledge Audit Log]
    end

    D -->|Validated Decision Packet| G[Downstream Enterprise Systems]

```
# Key Architectural Controls

## Deterministic Boundary
Ensures state transitions rely strictly on validated FSM state codes (`FSM_ERR_OVERRIDE_001`). This prevents model hallucination in downstream workflows.

## Transient Memory Flushing
Implements zero-knowledge retention by instantly purging unscripted raw text buffers upon state assignment.

## Executable Specification & PoC Assets

To validate the deterministic boundary and zero-knowledge data sovereignty model, an executable proof-of-concept is provided in the [`poc/`](./poc/) directory.

* **Interactive Sandbox:** Run the [`sia_fsm_boundary_sandbox.ipynb`](./poc/sia_fsm_boundary_sandbox.ipynb) notebook in Google Colab to test Cantonese jargon mapping, JSON schema enforcement, and transient flushing.
* **Data Contract:** Inspect [`decision-packet.schema.json`](./poc/decision-packet.schema.json) for the Draft-07 structural specification.
* **Telemetry Event Mock:** View [`mock-telemetry-event.json`](./poc/mock-telemetry-event.json) for a sample validated output.

---

***This document was structured with the help of AI, and curated by Sana.M***
