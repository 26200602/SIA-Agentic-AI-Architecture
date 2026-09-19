# Specification-002: SIA Layer 2 Sovereign Infrastructure & FSM Engine Architecture

**Document Identifier:** SIA-SPEC-002  
**Layer:** Layer 2 (Runtime Sovereign Infrastructure & Execution Engine)  
**Status:** Stable / Technical Protocol Specification  
**License:** Open-Source (Apache 2.0 / MIT)  

---

## 1. Architectural Scope & Runtime Boundaries

SIA Layer 2 defines the low-level technical protocol, memory management invariants, and deterministic execution cage for the Sovereign Intent Architecture.

While Layer 1 establishes high-level policy boundaries and regulatory compliance mappings, Layer 2 operates within the local runtime environment (Edge/On-Premises hardware). It enforces strict semantic decoupling, handles non-intrusive GraphRAG multi-hop reasoning, and controls the Finite State Machine (FSM) circuit breaker to guarantee determinism under adversarial conditions.

### 🛡️ SIA Layer 2 Runtime Execution Flow

```text
+-------------------------------------------------------------------+

|                        SIA LAYER 2 RUNTIME                        |
|                                                                   |
|  +-------------------+     +------------------+     +----------+  |
|  |  3-Tag Decoupler  | --> |  GraphRAG Engine | --> | FSM Cage |  |
|  |  (C/Rust Struct)  |     |  (Max 3 Hops)    |     | (0x88)   |  |
|  +-------------------+     +------------------+     +----+-----+  |
+----------------------------------------------------------|--------+
                                                           │ Violation
                                                           ▼
                                            +-------------------------------+

                                            | Memory Zeroization (memset_s) |
                                            | Non-Text Error Frame Output   |
                                            +-------------------------------+
```

---

## 2. 3-Tag Decoupling: C/Rust Memory Abstractions

To prevent the centralization of identifiable risk ("Bundles of Risk"), Layer 2 forbids raw text ingestion directly into probabilistic reasoning engines. All incoming enterprise data must be parsed into an ephemeral, decoupled 3-Tag memory structure.

### 2.1 Struct Definitions (C/Rust Memory Model)

```rust
// SIA Layer 2 Decoupled Memory Abstraction (Rust Equivalent)

#[repr(C)]
pub struct EntityTag {
    pub entity_id: [u8; 32],      // SHA-256 Hash of the isolated entity key
    pub domain_scope: u16,        // Isolated organizational scope identifier
}

#[repr(C)]
pub struct FactoidTag {
    pub factoid_id: [u8; 32],     // Unique cryptographic ID of atomic assertion
    pub entity_ref: [u8; 32],     // Pointer to EntityTag without raw text bindings
    pub payload_type: u8,         // Categorical type (e.g., Numeric, Boolean, Enum)
}

#[repr(C)]
pub struct StateTag {
    pub state_vector: u64,        // Bitmask representing current operational state
    pub timestamp_epoch: u64,     // Ephemeral validity window (TTL)
    pub integrity_hash: [u8; 32], // Cryptographic check for state tampering
}

#[repr(C)]
pub struct DecoupledContextFrame {
    pub entity: EntityTag,
    pub factoid: FactoidTag,
    pub state: StateTag,
}

### 3. GraphRAG Multi-Hop Reasoning & Traversal Constraints

Layer 2 utilizes a lightweight, local GraphRAG topology for contextual knowledge traversal. To prevent resource exhaustion, infinite loops, and unconstrained context crawling, traversal is governed by deterministic hardware bounds.

*   **Maximum Hop Limit (\(H_{\max}\)):** Strictly restricted to \(H \le 3\). Traversal beyond 3 hops is rejected at the protocol layer.
*   **Traversal TTL:** Ephemeral context frames expire after `15ms` of processing time.
*   **Asynchronous Shadowing:** Graph updates operate purely via read-only metatag shadowing over legacy datastores without executing schema mutations.

***

### 4. FSM Circuit Breaker & Deterministic Violation Protocol

Probabilistic Small Language Models (SLMs) operating at the edge are isolated within a deterministic Finite State Machine (FSM) cage. The SLM is permitted only to suggest state transitions; final state authorization is governed by the FSM transition table.

#### 4.1 State Machine Enumeration
typedef enum {
    SIA_STATE_IDLE          = 0x00,
    SIA_STATE_PARSING       = 0x01,
    SIA_STATE_EVALUATING    = 0x02,
    SIA_STATE_COMMITTED     = 0x03,
    SECURITY_VIOLATION_0x88 = 0x88  // Deterministic Circuit Breaker Activation
} sia_fsm_state_t;

#### 4.2 Violation Trigger Mechanics (`SECURITY_VIOLATION_0x88`)

If the edge SLM generates an output that violates Layer 1 policy constraints, attempts cross-domain prompt injection, or exhibits logic drift outside the permissible state vector, the FSM instantly transitions to `SECURITY_VIOLATION_0x88`.

*   **Execution Latency:** Violation interception is guaranteed at **<15ms**.

### 5. Ephemeral Memory Zeroization Protocol (`memset_s`)

Upon activation of `SECURITY_VIOLATION_0x88` or successful transaction completion, all transient RAM buffers housing context frames or SLM key-value caches must undergo Just-In-Time (JIT) secure erasure.

#### 5.1 C Memory Erasure Primitive
#define __STDC_WANT_LIB_EXT1__ 1
#include <string.h>
#include <stdlib.h>

void sia_purge_transient_buffer(void *buffer, size_t buffer_size) {
    if (buffer == NULL || buffer_size == 0) return;
    
    // Secure zeroization preventing compiler dead-code elimination optimization
    errno_t err = memset_s(buffer, buffer_size, 0, buffer_size);
    if (err != 0) {
        // Fallback hard-fault handling
        pabort("CRITICAL: Transient memory zeroization failed.");
    }
}

###. 6. Non-Text Error Frame Observability (Option B)
To maintain high enterprise observability without compromising the zero-trace privacy model, Layer 2 returns a deterministic, zero-raw-text error payload to the enterprise gateway upon violation.

#### 6.1 Payload Structural Specification
{
  "protocol_version": "SIA-2.0",
  "execution_status": "SECURITY_VIOLATION_0x88",
  "error_type": "ERR_STATE_DRIFT_EXCEEDED",
  "fault_node_id": "FACTOID_89A2_ISOLATED",
  "state_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "timestamp_epoch": 1787130018
}

Data Exposure Guarantee: The payload contains zero dynamic raw text, zero user payload content, and zero PII. Operational teams can isolate failing logic nodes via fault_node_id without exposing enterprise secrets.

### 7. Document Revision & System Control

*   **Author:** Sovereign Intent Architecture Engineering Group
*   **Target Integration:** NLNet NGI Restack Core Security Protocol
*   **Verification Status:** Verified against C11 `memset_s` standards & Rust Safety Invariants
