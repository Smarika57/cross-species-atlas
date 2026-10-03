
# Realistic Cross-Disease TFI Benchmarking Dataset
PRECOMPUTED_BENCHMARKING = [
    {"Disease Label": "Asthma", "MONDO Identifier": "MONDO:0004979", "Composite TFI Score": "84.2%", "Model Flag": "HIGH_FIDELITY"},
    {"Disease Label": "Breast Cancer", "MONDO Identifier": "MONDO:0007254", "Composite TFI Score": "76.5%", "Model Flag": "MODERATE_FIDELITY"},
    {"Disease Label": "Leukemia", "MONDO Identifier": "MONDO:0005059", "Composite TFI Score": "91.8%", "Model Flag": "HIGH_FIDELITY"},
    {"Disease Label": "Lung Cancer", "MONDO Identifier": "MONDO:0008903", "Composite TFI Score": "68.4%", "Model Flag": "MODERATE_FIDELITY"},
    {"Disease Label": "Cervical Cancer", "MONDO Identifier": "MONDO:0002974", "Composite TFI Score": "58.9%", "Model Flag": "LOW_FIDELITY"},
    {"Disease Label": "Hereditary Breast Carcinoma", "MONDO Identifier": "MONDO:0016419", "Composite TFI Score": "88.1%", "Model Flag": "HIGH_FIDELITY"},
    {"Disease Label": "Liver Cancer", "MONDO Identifier": "MONDO:0002691", "Composite TFI Score": "62.3%", "Model Flag": "LOW_FIDELITY"},
    {"Disease Label": "Rheumatoid Arthritis", "MONDO Identifier": "MONDO:0008382", "Composite TFI Score": "79.4%", "Model Flag": "MODERATE_FIDELITY"},
    {"Disease Label": "Inflammatory Bowel Disease", "MONDO Identifier": "MONDO:0005265", "Composite TFI Score": "72.0%", "Model Flag": "MODERATE_FIDELITY"},
    {"Disease Label": "Glioblastoma", "MONDO Identifier": "MONDO:0018177", "Composite TFI Score": "54.6%", "Model Flag": "LOW_FIDELITY"}
]

import streamlit as st
st.markdown('''
<style>
.stApp {
    background-color: #FAFAFA !important;
    background-image: 
        radial-gradient(circle at 15% 15%, rgba(2, 132, 199, 0.05) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(30, 58, 138, 0.04) 0%, transparent 40%),
        linear-gradient(rgba(226, 232, 240, 0.4) 1px, transparent 1px),
        linear-gradient(90deg, rgba(226, 232, 240, 0.4) 1px, transparent 1px) !important;
    background-size: 100% 100%, 100% 100%, 30px 30px, 30px 30px !important;
}

.block-container {
    padding-top: 2rem !important;
}
</style>
''', unsafe_allow_html=True)
import streamlit as st
st.markdown('''
<style>
/* Remove default margin padding */
.block-container {
    padding-top: 2rem !important;
}

/* Base Portal Background with subtle single-cell / genomic grid overlay */
.stApp {
    background-color: #FAFAFA !important;
    background-image: 
        radial-gradient(circle at 15% 15%, rgba(2, 132, 199, 0.04) 0%, transparent 40%),
        radial-gradient(circle at 85% 85%, rgba(30, 58, 138, 0.03) 0%, transparent 40%),
        linear-gradient(rgba(226, 232, 240, 0.3) 1px, transparent 1px),
        linear-gradient(90deg, rgba(226, 232, 240, 0.3) 1px, transparent 1px) !important;
    background-size: 100% 100%, 100% 100%, 30px 30px, 30px 30px !important;
}

/* Sidebar Institutional Styling */
[data-testid="stSidebar"] {
    background-color: #F8FAFC !important;
    border-right: 1px solid #E2E8F0 !important;
}

/* Metric Cards - Clean White Panels */
[data-testid="stMetric"], div[style*="border"] {
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 6px !important;
    padding: 12px 16px !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03) !important;
}

/* Metric Labels */
[data-testid="stMetricLabel"] {
    color: #475569 !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}

/* Deep Blue Monospace Metric Values */
[data-testid="stMetricValue"], div[style*="font-size: 2"] {
    color: #0284C7 !important;
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace !important;
    font-size: 1.8rem !important;
    font-weight: 700 !important;
}
</style>
''', unsafe_allow_html=True)
import streamlit as st
st.markdown('''
<style>
/* Base Portal Background */
.stApp {
    background-color: #FAFAFA !important;
}

/* Sidebar Institutional Styling */
[data-testid="stSidebar"] {
    background-color: #F1F5F9 !important;
    border-right: 1px solid #CBD5E1 !important;
}

/* Header Container Adjustments */
header[data-testid="stHeader"] {
    background-color: #FAFAFA !important;
}

/* Metric Cards - Dense NCBI Style */
[data-testid="stMetric"], div[style*="border"] {
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 4px !important;
    padding: 12px 16px !important;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03) !important;
}

/* Metric Labels */
[data-testid="stMetricLabel"] {
    color: #475569 !important;
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}

/* Monospace Scientific Values */
[data-testid="stMetricValue"], div[style*="font-size: 2"] {
    color: #0F172A !important;
    font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace !important;
    font-size: 1.8rem !important;
    font-weight: 700 !important;
}

/* Clean Form Input Container */
[data-testid="stForm"], div[data-testid="stVerticalBlock"] > div[style*="background"] {
    background-color: #F8FAFC !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 6px !important;
}

/* Dataframe Clinical Formatting */
[data-testid="stDataFrame"] {
    border: 1px solid #CBD5E1 !important;
    border-radius: 4px !important;
}

/* Table Header Customization */
div[data-testid="stTable"] table {
    width: 100% !important;
    border-collapse: collapse !important;
}

div[data-testid="stTable"] th {
    background-color: #1E293B !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
    padding: 8px 12px !important;
    font-size: 0.85rem !important;
}

div[data-testid="stTable"] td {
    padding: 8px 12px !important;
    border-bottom: 1px solid #E2E8F0 !important;
    font-size: 0.85rem !important;
}

/* Button Styling (NCBI Action Primary) */
.stButton > button {
    background-color: #0284C7 !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
    border-radius: 4px !important;
    border: none !important;
    padding: 6px 16px !important;
}

.stButton > button:hover {
    background-color: #0369A1 !important;
}
</style>
''', unsafe_allow_html=True)
st.markdown('''
<div style="background-color: #0F172A; color: #FFFFFF; padding: 8px 20px; font-size: 0.8rem; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 3px solid #0284C7; font-family: sans-serif;">
    <div>
        <strong style="color: #38BDF8;">NIH / NCBI / FAIR Data Portal</strong> &nbsp;|&nbsp; <span>Cross-Species Translational Fidelity Engine</span>
    </div>
    <div>
        <span style="background-color: #1E293B; padding: 2px 8px; border-radius: 3px; font-family: monospace; color: #38BDF8;">v1.4.2</span>
    </div>
</div>
''', unsafe_allow_html=True)
import streamlit as st
st.markdown('''
<style>
/* App White Background */
.stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background-color: #FFFFFF !important;
}

/* Force ALL Card Containers to White Background with Blue Text */
div[style*="border"], div[style*="border-radius"], div[style*="padding"], [data-testid="stMetric"] {
    background-color: #FFFFFF !important;
    background: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 8px !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
}

/* Metric Header Text */
div[style*="font-size"][style*="uppercase"], [data-testid="stMetricLabel"] {
    color: #475569 !important;
    font-weight: 600 !important;
}

/* Metric Value Numbers - Deep Blue */
div[style*="font-size: 2"], div[style*="font-size:2"], [data-testid="stMetricValue"] {
    color: #0284C7 !important;
    font-weight: 800 !important;
}
</style>
''', unsafe_allow_html=True)
import streamlit as st
st.markdown('''
<style>
/* Reset container background */
.stApp {
    background-color: #FFFFFF;
}

/* Metric Container Light Cards */
[data-testid="stMetric"], div[data-testid="metric-container"], .metric-card {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 6px !important;
    padding: 12px 16px !important;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
}

[data-testid="stMetricLabel"] {
    color: #0284C7 !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
}

[data-testid="stMetricValue"] {
    color: #0284C7 !important;
    font-size: 1.75rem !important;
    font-weight: 700 !important;
}

/* Status banners */
.stAlert {
    border-radius: 6px !important;
}

/* Sidebar clean border */
[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E2E8F0 !important;
}
</style>
''', unsafe_allow_html=True)
import streamlit as st
import json, os, sqlite3
import pandas as pd
from datetime import datetime
from ontology_lookup import lookup_disease_mondo, BioinformaticsValidationError
from pipeline_engine import execute_on_demand_pipeline
from divergence_engine import analyze_divergence
from export_engine import generate_regulatory_pdf
from stats_engine import calculate_tfi_confidence
from database import init_db, get_all_cached_diseases, get_all_submissions, update_submission_status, add_submission
from retrospective_validation import GROUND_TRUTH_CASES

init_db()

def init_audit_db():
    conn = sqlite3.connect("atlas_audit.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT, disease TEXT, mondo_id TEXT, tfi_score REAL, event_type TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_event(disease, mondo_id, tfi_score, event_type):
    conn = sqlite3.connect("atlas_audit.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO audit_logs (timestamp, disease, mondo_id, tfi_score, event_type)
        VALUES (?, ?, ?, ?, ?)
    ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), disease, mondo_id, tfi_score, event_type))
    conn.commit()
    conn.close()

init_audit_db()

st.markdown('''
<style>
/* Main app white background */
.stApp {
    background-color: #FFFFFF !important;
}

/* Streamlit Native Metric Cards & Custom Container Cards */
[data-testid="stMetric"], div[data-testid="metric-container"], .metric-card, .css-1r6slb0, .css-1wrcr25 {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 8px !important;
    padding: 16px !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
}

/* Metric Label Header */
[data-testid="stMetricLabel"] {
    color: #475569 !important;
    font-size: 0.875rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
}

/* Metric Value: Bold Deep Blue Accent */
[data-testid="stMetricValue"] {
    color: #1E3A8A !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
}

/* Custom HTML card overrides inside st.markdown */
div[style*="background-color"] {
    background-color: #FFFFFF !important;
    color: #0284C7 !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 8px !important;
}
</style>
''', unsafe_allow_html=True)
st.markdown('''
<style>
/* App background reset */
.stApp, [data-testid="stAppViewContainer"] {
    background-color: #FFFFFF !important;
}

/* Sidebar light reset */
[data-testid="stSidebar"], section[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E2E8F0 !important;
}

/* Force any custom HTML card container to white background */
div[style*="background"], div[style*="background-color"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
    border-radius: 8px !important;
}

/* Force dark titles and deep blue percentage values */
div[style*="color: #"], div[style*="color:#"], p, span, h1, h2, h3 {
    color: #0284C7;
}

/* Target deep blue text for numbers and scores */
.metric-value, [data-testid="stMetricValue"] {
    color: #1E3A8A !important;
    font-weight: 800 !important;
}
</style>
''', unsafe_allow_html=True)
st.markdown('''
<style>
/* Main app white background */
.stApp, [data-testid="stAppViewContainer"] {
    background-color: #FFFFFF !important;
}

/* Sidebar styling */
[data-testid="stSidebar"], section[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E2E8F0 !important;
}

/* Force Streamlit native metrics to white card layout */
[data-testid="stMetric"], div[data-testid="metric-container"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 8px !important;
    padding: 16px !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
}

[data-testid="stMetricLabel"] {
    color: #475569 !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
}

[data-testid="stMetricValue"] {
    color: #0284C7 !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
}

/* Force custom markdown div cards to Pure White with Deep Blue Values */
div[style*="border-radius"], div[style*="padding"] {
    background-color: #FFFFFF !important;
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
}
</style>
''', unsafe_allow_html=True)
st.set_page_config(page_title='Cross-Species Atlas', layout='wide')

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'IBM Plex Sans', -apple-system, sans-serif; color: #E7ECF5; background-color: #FFFFFF; }
    code, pre, .stDataFrame, [data-testid="stMetricValue"] { font-family: 'IBM Plex Mono', monospace !important; }
    [data-testid="stMetric"], .stDataFrame { background-color: #FFFFFF !important; border: 1px solid #24304A !important; border-radius: 4px !important; }
    [data-testid="stMetricValue"] { color: #4FD1C5 !important; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

st.title("Cross-Species Translational Fidelity Atlas")
st.caption("A FAIR-compliant, ontology-standardized platform for benchmarking preclinical animal models against human single-cell data.")

cached_diseases = get_all_cached_diseases()

nav = st.sidebar.radio("Navigation View", [
    "Single Disease Deep-Dive", 
    "Retrospective Clinical Validation", 
    "Cross-Disease TFI Benchmarking", 
    "Community Provenance Submission",
    "Admin Curation Queue",
    "Audit Trail Logs"
])

if nav == "Single Disease Deep-Dive":
    st.header("Single Disease Model Deep-Dive")
    
    col_search, col_preset = st.columns([2, 1])
    with col_preset:
        preset_choice = st.selectbox(
            "Quick Select Precomputed Dataset",
            ["-- Select Precomputed --"] + [d["disease"] for d in cached_diseases]
        )
    with col_search:
        user_query = st.text_input(
            "Search Any Disease / Model (e.g. 'Brain Cancer', 'Leukemia', 'Asthma')",
            value=preset_choice if preset_choice != "-- Select Precomputed --" else "Asthma"
        )

    matched_disease = None
    if user_query:
        try:
            matched_disease = execute_on_demand_pipeline(user_query)
        except (BioinformaticsValidationError, ValueError) as e:
            st.error(f" Bioinformatics Validation Error: {str(e)}")
            st.stop()
        except Exception as e:
            st.error(f" Pipeline Execution Error: {str(e)}")
            st.stop()

    disease = matched_disease
    ont = disease.get("ontology", {})
    log_event(disease["disease"], ont.get("disease_id"), disease.get("composite_tfi"), "PIPELINE_VIEW")

    divergence_res = analyze_divergence(disease["disease"], disease.get("target_genes", []))
    pdf_bytes = generate_regulatory_pdf(disease, divergence_res)
    df_genes = pd.DataFrame(disease.get("target_genes", []))
    csv_bytes = df_genes.to_csv(index=False).encode('utf-8')

    c_col1, c_col2, c_col3 = st.columns([2, 1, 1])
    with c_col1:
        st.success(f"** Status:** Active Payload Loaded for `{disease['disease']}`")
    with c_col2:
        if st.download_button(" Download PDF Report", pdf_bytes, f"{disease['disease']}_TFI_Report.pdf", "application/pdf"):
            log_event(disease["disease"], ont.get("disease_id"), disease.get("composite_tfi"), "PDF_REPORT_EXPORT")
    with c_col3:
        if st.download_button(" Download Gene Matrix CSV", csv_bytes, f"{disease['disease']}_target_genes.csv", "text/csv"):
            log_event(disease["disease"], ont.get("disease_id"), disease.get("composite_tfi"), "CSV_MATRIX_EXPORT")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Composite TFI Score", f"{disease['composite_tfi']}%")
    col2.metric("Signature Subscore", f"{disease['signature_subscore']}%")
    col3.metric("Integration Subscore", f"{disease['integration_subscore']}%")
    col4.metric("Model Flag", disease['flag'])

    st.subheader("Why Does This Model Diverge? (Divergence Driver Analysis)")
    st.info(divergence_res["narrative"])

    st.markdown("#### Top Cross-Species Discordant Target Genes")
    st.dataframe(df_genes, use_container_width=True)

elif nav == "Retrospective Clinical Validation":
    st.header("Retrospective Validation against Documented Human Trial Outcomes")
    st.dataframe(pd.DataFrame(GROUND_TRUTH_CASES), use_container_width=True)

elif nav == "Cross-Disease TFI Benchmarking":
    st.header("Cross-Disease TFI Benchmarking Overview")
    if not cached_diseases:
        st.info("No cached benchmarks available yet. Run a search in 'Single Disease Deep-Dive' to populate.")
    else:
        records = []
        for d in cached_diseases:
            records.append({
                "Disease Label": d["disease"],
                "MONDO Identifier": d.get("ontology", {}).get("disease_id", "N/A"),
                "Composite TFI Score": f"{d['composite_tfi']}%",
                "Model Flag": d["flag"]
            })
        st.dataframe(pd.DataFrame(records), use_container_width=True)

elif nav == "Community Provenance Submission":
    st.header("Community Disease/Model Submission Portal")
    with st.form("submission_form"):
        orcid = st.text_input("Submitter ORCID ID", "0000-0002-1825-0097")
        geo = st.text_input("GEO Accession Number", "GSE136103")
        mondo = st.text_input("Disease MONDO ID", "MONDO:0005359")
        uberon = st.text_input("Organ UBERON ID", "UBERON:0002107")
        ncbi = st.text_input("Species NCBI Taxonomy ID", "NCBITaxon:10090")
        submitted = st.form_submit_button("Submit Dataset for Review")
        
        if submitted:
            sub_id = add_submission({
                "submitter_orcid": orcid,
                "geo_accession": geo,
                "disease_mondo_id": mondo,
                "organ_uberon_id": uberon,
                "species_ncbi_id": ncbi
            })
            log_event(f"Submission {sub_id}", mondo, 0.0, "COMMUNITY_SUBMISSION")
            st.success(f" Submission Saved to Database! Submission ID: `{sub_id}`")

elif nav == "Admin Curation Queue":
    st.header(" Admin Curation Queue")
    
    if "admin_authenticated" not in st.session_state:
        st.session_state["admin_authenticated"] = False

    if not st.session_state["admin_authenticated"]:
        admin_pass = st.text_input("Enter Admin Access Key", type="password")
        if st.button("Authenticate Admin Access"):
            if admin_pass == "admin123":
                st.session_state["admin_authenticated"] = True
                st.success("Access Granted!")
                st.rerun()
            else:
                st.error("Invalid Admin Key.")
        st.stop()

    submissions = get_all_submissions()
    if not submissions:
        st.info("No community submissions found in queue.")
    else:
        st.dataframe(pd.DataFrame(submissions), use_container_width=True)
        sub_ids = [s["submission_id"] for s in submissions]
        selected_sub_id = st.selectbox("Select Submission ID", sub_ids)
        new_status = st.selectbox("Update Decision", ["APPROVED", "REJECTED", "PENDING_REVIEW"])
        notes = st.text_input("Reviewer Notes", "Verified accession & MONDO alignment.")
        if st.button("Commit Decision"):
            update_submission_status(selected_sub_id, new_status, notes)
            log_event(f"Review {selected_sub_id}", f"Status: {new_status}", 0.0, "ADMIN_CURATION_DECISION")
            st.success(f"Updated status for `{selected_sub_id}` to {new_status}!")
            st.rerun()

elif nav == "Audit Trail Logs":
    st.header("FAIR Data Audit Trail Logs")
    conn = sqlite3.connect("atlas_audit.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, timestamp, disease, mondo_id, tfi_score, event_type FROM audit_logs ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    st.dataframe(pd.DataFrame(rows, columns=["Log ID", "Timestamp", "Disease / Entity", "MONDO ID / Metadata", "TFI Score", "Event Type"]), use_container_width=True)
