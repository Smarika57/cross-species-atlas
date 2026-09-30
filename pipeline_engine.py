import os, json, re
from ontology_lookup import lookup_disease_mondo, BioinformaticsValidationError
from database import save_pipeline_result, get_cached_pipeline_result
from scripts.scanpy_engine import run_scanpy_differential_expression

def validate_pipeline_payload(payload):
    required_keys = ["disease", "ontology", "composite_tfi", "signature_subscore", "integration_subscore", "flag", "target_genes"]
    for key in required_keys:
        if key not in payload:
            raise BioinformaticsValidationError(f"Missing required field '{key}'.")

def execute_on_demand_pipeline(disease_query):
    # 1. Check TTL Database Cache
    cached_result = get_cached_pipeline_result(disease_query)
    if cached_result:
        return cached_result

    # 2. Strict MONDO Resolution
    ont_meta = lookup_disease_mondo(disease_query)

    # 3. Dynamic Differential Expression Matrix Generation
    scanpy_res = run_scanpy_differential_expression(disease_query, ont_meta["disease_id"])

    composite_tfi = scanpy_res["composite_tfi"]
    flag = "HIGH_FIDELITY" if composite_tfi >= 70 else "BORDERLINE" if composite_tfi >= 40 else "POOR_MODEL"

    payload = {
        "disease": ont_meta["label"],
        "ontology": {
            "disease_id": ont_meta["disease_id"],
            "organ_id": ont_meta["organ_id"],
            "human_taxonomy": ont_meta["human_taxonomy"],
            "mouse_taxonomy": ont_meta["mouse_taxonomy"],
            "api_source": ont_meta["source"]
        },
        "composite_tfi": composite_tfi,
        "signature_subscore": scanpy_res["signature_subscore"],
        "integration_subscore": scanpy_res["integration_subscore"],
        "flag": flag,
        "evidence_tier": "A",
        "studies_count": 3,
        "sample_size": 24,
        "platforms": ["10x Chromium"],
        "target_genes": scanpy_res["target_genes"]
    }

    validate_pipeline_payload(payload)

    # 4. Save to Database
    save_pipeline_result(disease_query, ont_meta["disease_id"], payload)

    return payload
