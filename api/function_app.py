import azure.functions as func
import json
from pathlib import Path
from typing import Any


app = func.FunctionApp()


def validate_submission(data: dict[str, Any]) -> tuple[bool, dict[str, str]]:
    """Validate submission data. Returns (is_valid, errors_dict)."""
    errors = {}

    if not data.get("name", "").strip():
        errors["name"] = "Name is required."
    if not data.get("email", "").strip():
        errors["email"] = "Email is required."
    elif "@" not in data.get("email", ""):
        errors["email"] = "Email must be valid."
    if not data.get("id", "").strip():
        errors["id"] = "ID is required."
    if not data.get("phone", "").strip():
        errors["phone"] = "Phone is required."

    return len(errors) == 0, errors


def save_submission_local(data: dict[str, Any]) -> None:
    """Save submission to local JSON file (for local development)."""
    file_path = Path("/tmp/submissions.json")  # Use /tmp for Azure Functions container

    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as f:
            submissions = json.load(f)
        if not isinstance(submissions, list):
            submissions = []
    else:
        submissions = []

    submissions.append(data)

    with file_path.open("w", encoding="utf-8") as f:
        json.dump(submissions, f, indent=2)


@app.route(route="submissions", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def submissions(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP-triggered function to accept form submissions.
    
    Expected POST payload:
    {
      "name": "string",
      "email": "string",
      "id": "string",
      "phone": "string"
    }
    """
    try:
        data = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"message": "Invalid JSON"}),
            status_code=400,
            mimetype="application/json",
        )

    # Validate
    is_valid, errors = validate_submission(data)
    if not is_valid:
        return func.HttpResponse(
            json.dumps(
                {"message": "Validation failed.", "errors": errors}
            ),
            status_code=400,
            mimetype="application/json",
        )

    # Save
    try:
        save_submission_local(data)
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"message": f"Error saving submission: {str(e)}"}),
            status_code=500,
            mimetype="application/json",
        )

    return func.HttpResponse(
        json.dumps({"message": "Submission saved successfully."}),
        status_code=200,
        mimetype="application/json",
    )
