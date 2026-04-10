# Knowledge-Transfer-Sessions

Simple Django website with a form that collects required user details and stores each submission in a JSON file.

## Overview

This project provides a single-page form with the following mandatory fields:

- Name
- Email
- ID
- Phone

When the form is submitted successfully, the entry is appended to `data/submissions.json`.

## Architecture

- Backend and UI: Django templates
- Form validation: Django `forms.Form` (all fields required)
- Persistence: JSON file on disk (`data/submissions.json`)

## Prerequisites

- Python 3.11+
- pip

## Setup & Installation

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Locally

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Running Tests

```bash
python manage.py test
```

## Environment Variables

No environment variables are required for local development in the current setup.

## Deployment

### Azure Static Web Apps

The GitHub Actions workflow for Static Web Apps is configured to skip Oryx app build (`skip_app_build: true`) to avoid Node build-script detection errors in this Python repository.

Important: this project is a Django server-rendered app. Azure Static Web Apps is intended for static frontends (and optional Azure Functions APIs), so Django runtime behavior is not hosted there.

If you need the full form submission behavior in Azure, deploy this project to Azure App Service instead.

## Data File

- File: `data/submissions.json`
- Format: JSON array
- Example record:

```json
{
	"name": "Jane Doe",
	"email": "jane@example.com",
	"id": "ABC123",
	"phone": "1234567890"
}
```
