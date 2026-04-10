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
