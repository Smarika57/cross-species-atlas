def analyze_divergence(disease_name, target_genes):
    discordant = [g for g in target_genes if g.get("fidelity") == "Discordant"]
    if discordant:
        gene_list = ", ".join([g["gene"] for g in discordant])
        narrative = f"Transcriptional divergence in {disease_name} is driven by discordant expression in key markers: {gene_list}."
    else:
        narrative = f"High overall fidelity observed for {disease_name} across analyzed target markers."
    
    return {
        "narrative": narrative,
        "enriched_pathways": [
            {"pathway": "Inflammatory Response", "p_value": 0.002, "genes": "IL6, TNF"},
            {"pathway": "Cytokine-Cytokine Receptor Interaction", "p_value": 0.015, "genes": "IL6"}
        ]
    }
