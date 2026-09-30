import sqlite3, json
from datetime import datetime, timedelta

DB_FILE = "atlas_data.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pipeline_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            disease_query TEXT UNIQUE,
            mondo_id TEXT,
            payload_json TEXT,
            created_at TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS community_submissions (
            submission_id TEXT PRIMARY KEY,
            submitter_orcid TEXT,
            geo_accession TEXT,
            disease_mondo_id TEXT,
            organ_uberon_id TEXT,
            species_ncbi_id TEXT,
            status TEXT,
            notes TEXT,
            submitted_at TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_pipeline_result(disease_query, mondo_id, payload):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO pipeline_results (disease_query, mondo_id, payload_json, created_at)
        VALUES (?, ?, ?, ?)
    ''', (disease_query.lower(), mondo_id, json.dumps(payload), datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_cached_pipeline_result(disease_query, ttl_days=7):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT payload_json, created_at FROM pipeline_results WHERE disease_query = ?
    ''', (disease_query.lower(),))
    row = cursor.fetchone()
    conn.close()

    if row:
        payload_json, created_at_str = row
        created_at = datetime.fromisoformat(created_at_str)
        if datetime.now() - created_at < timedelta(days=ttl_days):
            return json.loads(payload_json)
    return None

def get_all_cached_diseases():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT payload_json FROM pipeline_results')
    rows = cursor.fetchall()
    conn.close()
    return [json.loads(r[0]) for r in rows]

def add_submission(sub):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    sub_id = f"SUB-{int(datetime.now().timestamp())}"
    cursor.execute('''
        INSERT INTO community_submissions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (sub_id, sub["submitter_orcid"], sub["geo_accession"], sub["disease_mondo_id"],
          sub["organ_uberon_id"], sub["species_ncbi_id"], "PENDING_REVIEW", "", datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return sub_id

def get_all_submissions():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT submission_id, submitter_orcid, geo_accession, disease_mondo_id, status FROM community_submissions')
    rows = cursor.fetchall()
    conn.close()
    return [{"submission_id": r[0], "submitter_orcid": r[1], "geo_accession": r[2], "disease_mondo_id": r[3], "status": r[4]} for r in rows]

def update_submission_status(sub_id, status, notes):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('UPDATE community_submissions SET status = ?, notes = ? WHERE submission_id = ?', (status, notes, sub_id))
    conn.commit()
    conn.close()
