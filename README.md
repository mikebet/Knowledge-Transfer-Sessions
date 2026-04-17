# Michael Bernardo — Portfolio

A modern, responsive portfolio website built with vanilla HTML, CSS, and JavaScript. Features a dark/light theme, scroll animations, and a clean design optimized for Azure Static Web Apps.

## Overview

A single-page portfolio/CV site showcasing skills, experience, projects, and education with an engaging animated UI.

## Architecture

- **Frontend**: Static HTML/CSS/JavaScript (deployed to Azure Static Web Apps)
- **Hosting**: Azure Static Web Apps
- **Routing**: `staticwebapp.config.json` with SPA fallback

```
User Browser
    ↓
Azure Static Web Apps (CDN)
    ↓
index.html + styles.css + script.js
```

## Features

- Dark/light theme toggle with local storage persistence
- Smooth scroll-reveal animations using Intersection Observer
- Animated stat counters
- Responsive mobile navigation
- Floating background gradient shapes
- Active navigation link tracking
- Scroll-to-top button

## Prerequisites

- A modern web browser
- (Optional) Azure CLI for deployment

## Setup & Installation

No build step required. This is a static site.

```bash
git clone <repo-url>
cd Knowledge-Transfer-Sessions
```

## Running Locally

Open `frontend/index.html` directly in your browser, or serve it with any static file server:

```bash
cd frontend
python -m http.server 8000
```

Then open `http://localhost:8000/` in your browser.

## Customization

Edit `frontend/index.html` to update:
- Your name, tagline, and description in the **Hero** section
- About me text and stats in the **About** section
- Skill tags in the **Skills** section
- Job history in the **Experience** timeline
- Project cards in the **Projects** section
- Degrees and certifications in **Education**
- Email and social links in **Contact**

## Deployment

### Azure Static Web Apps

1. Push to `main` branch — CI/CD pipeline triggers automatically.
2. GitHub Actions deploys `frontend/` to Azure Static Web Apps.
3. `staticwebapp.config.json` handles SPA routing and security headers.

### Azure Infrastructure

- **Frontend**: Azure Static Web Apps — `<resource-name>`
- **Region**: `<e.g., East US 2>`

## Project Structure

```
├── frontend/
│   ├── index.html             # Portfolio page
│   ├── styles.css             # Theme + layout + animations
│   └── script.js              # Scroll reveal, theme toggle, nav
├── staticwebapp.config.json   # SWA routing & security headers
├── .github/workflows/         # CI/CD pipeline
└── README.md
```

## License

See [LICENSE](LICENSE).
