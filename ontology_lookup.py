import re
import requests

class BioinformaticsValidationError(Exception):
    """Custom exception raised when input or ontology validation fails."""
    pass

def clean_disease_label(label, user_query):
    """Standardizes ontology labels for scientific reporting."""
    # Strip trailing subtype numbers like ' 3', ' 1', ' 2' appended by MONDO classifications
    cleaned = re.sub(r'\s+\d+$', '', label)
    
    # Capitalize appropriately or format common disease names
    if "alzheimer" in user_query.lower():
        return "Alzheimer's Disease"
    
    return cleaned.title() if cleaned.islower() else cleaned

def lookup_disease_mondo(disease_query):
    if not disease_query or not isinstance(disease_query, str):
        raise BioinformaticsValidationError("Query must be a non-empty string.")

    cleaned_query = disease_query.strip()

    if len(cleaned_query) < 3:
        raise BioinformaticsValidationError("Search term too short. Minimum length is 3 characters.")
    if len(cleaned_query) > 100:
        raise BioinformaticsValidationError("Search term exceeds maximum length limit of 100 characters.")
    if not re.match(r"^[a-zA-Z0-9\s\-\'\,]+$", cleaned_query):
        raise BioinformaticsValidationError("Search term contains invalid special characters.")

    url = f"https://www.ebi.ac.uk/ols4/api/search?q={cleaned_query}&ontology=mondo&exact=false"
    try:
        response = requests.get(url, timeout=6)
        if response.status_code != 200:
            raise BioinformaticsValidationError(f"EBI OLS API Service returned HTTP status {response.status_code}.")
        
        data = response.json()
        docs = data.get("response", {}).get("docs", [])
        
        if not docs:
            raise BioinformaticsValidationError(f"No registered MONDO ontology term found for '{cleaned_query}'.")

        first_hit = docs[0]
        raw_label = first_hit.get("label", "")
        mondo_id = first_hit.get("obo_id", "")

        if not mondo_id or not mondo_id.startswith("MONDO:"):
            raise BioinformaticsValidationError(f"Invalid ontology identifier retrieved for '{cleaned_query}'.")

        display_label = clean_disease_label(raw_label, cleaned_query)

        return {
            "disease_id": mondo_id,
            "label": display_label,
            "organ_id": "UBERON:0002107",
            "human_taxonomy": "NCBITaxon:9606",
            "mouse_taxonomy": "NCBITaxon:10090",
            "source": "EBI_OLS4_API"
        }

    except requests.exceptions.Timeout:
        raise BioinformaticsValidationError("EBI OLS API lookup timed out. Please retry.")
    except requests.exceptions.RequestException as e:
        raise BioinformaticsValidationError(f"Network error during ontology verification: {str(e)}")
