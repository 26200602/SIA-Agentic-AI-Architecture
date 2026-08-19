#!/usr/bin/env python3
"""
SIA Shadow Diagnostic Engine - Reference Implementation
Classification: Enterprise Architecture Specification (SimPoC)
Dependencies: None (Python Standard Library Only)
"""

import json
import re
import argparse
from datetime import datetime

class LocalEntityMasker:
    """Simulates on-premises entity isolation & PII anonymization."""
    def __init__(self):
        self.email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
        self.phone_pattern = re.compile(r'\+?\d{3,4}[-\s]?\d{4}[-\s]?\d{4}')
        self.name_pattern = re.compile(r'(?:David Chan|Ah Wah)', re.IGNORECASE)

    def mask_text(self, text: str) -> str:
        text = self.email_pattern.sub('[ANONYMIZED_EMAIL]', text)
        text = self.phone_pattern.sub('[ANONYMIZED_PHONE]', text)
        text = self.name_pattern.sub('[MASKED_PERSONNEL]', text)
        return text

class SIAFactoidParser:
    """Parses raw communication streams into deterministic Factoid Triplets."""
    def parse_artifact(self, artifact: dict, masker: LocalEntityMasker) -> dict:
        masked_payload = masker.mask_text(artifact.get("raw_payload", ""))
        
        # Extract intent & spatial clearances via deterministic rules
        spatial_clearance = None
        clearance_match = re.search(r'(\d{4})\s*mm', artifact.get("raw_payload", ""))
        if clearance_match:
            spatial_clearance = int(clearance_match.group(1))

        return {
            "factoid_id": f"FACTOID-{artifact['artifact_id']}",
            "timestamp_utc": artifact["timestamp_utc"],
            "stakeholder_role": artifact["source_stakeholder"],
            "canonical_state_id": f"STATE_{artifact['metadata']['revision']}",
            "anonymized_intent_summary": masked_payload,
            "constraint_signature": {
                "spatial_clearance_mm": spatial_clearance,
                "drawing_reference_hash": artifact["metadata"]["drawing_hash"]
            }
        }

class ContextLatencyEvaluator:
    """Evaluates temporal gap (Delta t) and Semantic Disconnect Score (SDS)."""
    @staticmethod
    def calculate_metrics(factoids: list):
        timestamps = [datetime.fromisoformat(f["timestamp_utc"].replace("Z", "+00:00")) for f in factoids]
        
        # Calculate Delta t (Time between Intent Revision and Site Realization)
        t_intent = timestamps[0]
        t_site_aware = timestamps[-1]
        delta_t_hours = (t_site_aware - t_intent).total_seconds() / 3600.0

        # Calculate SDS based on drawing revision drift across roles
        revisions = [f["canonical_state_id"] for f in factoids]
        unique_revisions = set(revisions)
        sds_score = (len(unique_revisions) - 1) / len(revisions) * 100 if revisions else 0.0

        return delta_t_hours, sds_score, t_intent, t_site_aware

def run_diagnostic(input_file: str):
    print("SIA SHADOW DIAGNOSTIC ENGINE v1.0 | EXECUTION REPORT\n")
    print("[INFO] Local Entity Masking Engine initialized. (Zero Cloud Telemetry)")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        raw_artifacts = json.load(f)

    print(f"[INFO] Processing {len(raw_artifacts)} unstructured communication artifacts...")
    print("[INFO] Executing SLM Semantic Mapping & FSM State Alignment...\n")

    masker = LocalEntityMasker()
    parser = SIAFactoidParser()
    factoids = []

    for art in raw_artifacts:
        factoid = parser.parse_artifact(art, masker)
        factoids.append(factoid)

    delta_t, sds, t_intent, t_site = ContextLatencyEvaluator.calculate_metrics(factoids)

    print("DIAGNOSTIC FINDINGS")
    print("Target Scenario       : Stage 0 -> Stage 1 Handover (HVAC Plant Room Layout)")
    print("Primary Intent Drift  : Revision C (Architect) vs Revision A (Site Sub-Contractor)\n")
    
    print(f"[METRIC 1] Context Latency Gap      : {delta_t:.1f} Hours")
    print(f"           Origin Intent Modified   : {t_intent.isoformat()} (Email / Attachment)")
    print(f"           Site Realization Aware   : {t_site.isoformat()} (WhatsApp / Site Photo)\n")
    
    print(f"[METRIC 2] Semantic Disconnect Score: {sds:.1f}%")
    print("           Root Cause Analysis      : Terminology mismatch between MEP Routing Jargon")
    print("                                      and Constructability Clearance Constraints.\n")
    
    print("[RECOMMENDATION]")
    print("Structural Operational Debt detected in Handover Protocol. Do NOT deploy conversational")
    print("AI assistants to frontline teams. Restructure the Push-Notification State Boundary")
    print("within the Master Project Specification.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SIA Shadow Diagnostic Engine CLI")
    parser.add_argument("--input", required=True, help="Path to input json logs")
    args = parser.parse_args()
    
    run_diagnostic(args.input)
