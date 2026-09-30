# Cross-Species Translational Fidelity Atlas

![CI Pipeline](https://github.com/Smarika57/cross-species-atlas/actions/workflows/main.yml/badge.svg)

A FAIR-compliant, ontology-standardized platform for benchmarking preclinical animal models against human single-cell data.

## Features
- **Ontology Mapping**: Standardized using MONDO, UBERON, and NCBI Taxonomies.
- **FAIR Audit Trail**: SQLite-backed persistent audit logging for pipeline runs, community submissions, and admin curation decisions.
- **Containerized**: Built with Streamlit and Docker.

## Deployment & Usage

### Local Docker Run
```bash
docker build -t cross-species-atlas:v1 .
docker run -d -p 8501:8501 --name atlas_app cross-species-atlas:v1

