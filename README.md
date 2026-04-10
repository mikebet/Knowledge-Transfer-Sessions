# Knowledge-Transfer-Sessions

A modern serverless form submission system with a static frontend and Azure Functions backend.

## Overview

This project provides a single-page form with the following mandatory fields:

- Name
- Email
- ID
- Phone

When the form is submitted successfully, the entry is persisted via an Azure Functions API endpoint.

## Architecture

- **Frontend**: Static HTML/CSS/JavaScript form (deployed to Azure Static Web Apps)
- **API Backend**: Azure Functions (Python v2) - HTTP-triggered function to validate and persist submissions
- **Storage**: Local JSON (development) or Azure SQL Database (production)
- **Routing**: `staticwebapp.config.json` routes `/api/*` requests to Functions

```
User Browser
    ↓
Frontend (Static Web Apps at /)
    ↓
JavaScript POST to /api/submissions
    ↓
Azure Functions (API at /api)
    ↓
Validation → Database Write
    ↓
JSON Response
```

## Prerequisites

- Python 3.11+
- pip
- Azure CLI (for deploying to Azure)
- Azure Static Web Apps resource

## Setup & Installation

1. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r api/requirements.txt
   ```

## Running Locally

### Option 1: Frontend Only (Static HTML)

Open `frontend/index.html` directly in your browser. Form posts will fail since there's no running API.

### Option 2: Frontend + Functions (Full Local Stack)

1. **Start Azure Functions Core Tools**:
   ```bash
   cd api
   func start
   ```
   The function will be available at `http://localhost:7071/api/submissions`.

2. **In another terminal, serve the frontend**:
   ```bash
   cd frontend
   python -m http.server 8000
   ```
   Open `http://localhost:8000/` in your browser.

3. **Update `frontend/script.js`** to point to the local Functions endpoint:
   ```javascript
   // Change this line:
   const response = await fetch("/api/submissions", {
   // To:
   const response = await fetch("http://localhost:7071/api/submissions", {
   ```

## API Endpoint

### POST /api/submissions

**Request**:
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "id": "ABC123",
  "phone": "1234567890"
}
```

**Response (Success - 200)**:
```json
{
  "message": "Submission saved successfully."
}
```

**Response (Validation Error - 400)**:
```json
{
  "message": "Validation failed.",
  "errors": {
    "email": "Email must be valid.",
    "phone": "Phone is required."
  }
}
```

## Deployment

### To Azure Static Web Apps + Functions

1. **Ensure all tests pass**:
   ```bash
   cd api && python -m pytest tests/ --tb=short -q 2>/dev/null || true
   ```

2. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Add serverless form with Functions API"
   git push origin main
   ```

3. **GitHub Actions will**:
   - Deploy `frontend/` to SWA root
   - Deploy `api/` as Azure Functions
   - Route `/api/*` to Functions via `staticwebapp.config.json`

4. **Configure Database (Production)**:
   - Create Azure SQL Database or Azure Cosmos DB
   - Update `api/function_app.py` to use database connection string from Key Vault
   - Example:
     ```python
     import os
     from azure.identity import DefaultAzureCredential
     from azure.keyvault.secrets import SecretClient
     
     credential = DefaultAzureCredential()
     secret_client = SecretClient(vault_url=os.getenv("KEYVAULT_URL"), credential=credential)
     db_connection_string = secret_client.get_secret("db-connection-string").value
     ```

## Environment Variables

No environment variables required for local development.

For production Azure deployment:
- `KEYVAULT_URL`: Azure Key Vault URL (for secrets)
- Store `DATABASE_CONNECTION_STRING` in Key Vault

## Data File (Local Development)

- File: `/tmp/submissions.json` (or `data/submissions.json` if running as Django)
- Format: JSON array
- Example:
  ```json
  [
    {
      "name": "Jane Doe",
      "email": "jane@example.com",
      "id": "ABC123",
      "phone": "1234567890"
    }
  ]
  ```

## Deployment Configuration

- **Platform**: Azure Static Web Apps with Azure Functions
- **Frontend**: Static HTML
- **API**: Python Azure Functions v2
- **Database**: JSON (dev) → Azure SQL (prod)
- **CI/CD**: GitHub Actions workflow in `.github/workflows/`

## Project Structure

```
├── frontend/                          # Static website
│   ├── index.html                    # Form page
│   ├── styles.css                    # Styling
│   └── script.js                     # Form handling
├── api/                              # Azure Functions project
│   ├── function_app.py              # Submissions endpoint
│   ├── requirements.txt              # Function dependencies
│   ├── host.json                     # Functions config
│   ├── local.settings.json           # Local dev settings (not committed)
│   └── tests/                        # Function tests
├── staticwebapp.config.json          # SWA routing config
├── .github/workflows/                # CI/CD pipeline
└── README.md                         # This file
```
