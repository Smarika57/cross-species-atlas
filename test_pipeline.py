import pytest
import os
from ontology_lookup import lookup_disease_mondo, BioinformaticsValidationError
from stats_engine import calculate_tfi_confidence
from export_engine import generate_regulatory_pdf
from database import init_db, add_submission, get_all_submissions, update_submission_status

def test_short_and_invalid_character_queries():
    with pytest.raises(BioinformaticsValidationError, match="Minimum length"):
        lookup_disease_mondo("ab")

    with pytest.raises(BioinformaticsValidationError, match="invalid special characters"):
        lookup_disease_mondo("Asthma<script>")

def test_tfi_confidence_bounds():
    scores = [60.0, 62.0, 64.0, 66.0, 68.0]
    res = calculate_tfi_confidence(scores, n_bootstraps=500, ci=95)
    
    assert res["mean_tfi"] == 64.0
    assert res["ci_lower"] < res["mean_tfi"]
    assert res["ci_upper"] > res["mean_tfi"]

def test_database_crud_operations():
    init_db()
    sub_data = {
        "submitter_orcid": "0000-0002-1825-0097",
        "geo_accession": "GSE136103",
        "disease_mondo_id": "MONDO:0004979",
        "organ_uberon_id": "UBERON:0002107",
        "species_ncbi_id": "NCBITaxon:10090"
    }
    sub_id = add_submission(sub_data)
    assert sub_id.startswith("SUB-")
