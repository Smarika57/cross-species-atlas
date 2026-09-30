from database import add_submission, get_all_submissions, update_submission_status

def process_community_submission(submission_data):
    sub_id = add_submission(submission_data)
    return {
        "status": "ACCEPTED_FOR_CURATION",
        "message": "Dataset successfully saved to persistent database queue.",
        "submission": {
            "submission_id": sub_id,
            **submission_data
        }
    }
