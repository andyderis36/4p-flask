# 4P Flask

A simple Flask web application for recording and sharing daily 4P updates: Project, Progress, Problem, Plan. The app supports user accounts, profiles, and basic social features.

## Features

- User authentication (register, login, logout)
- User profile with profile photo upload
- CRUD for 4P posts (Project / Progress / Problem / Plan)
- Follow / unfollow other users
- Admin page to view user list
- Password reset via email
- Export data to Excel (.xlsx)

## Technologies

- Flask 2.x
- SQLAlchemy + Flask-Migrate
- Flask-Login, Flask-Mail, Flask-Bootstrap, Flask-Excel

## Quick Start

1. Create and activate a virtual environment:

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Windows (cmd)
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The application reads configuration from environment variables. Common variables:

- SECRET_KEY — Flask secret key
- DATABASE_URL — SQLAlchemy database URL (default: SQLite `app.db`)
- MAIL_SERVER, MAIL_PORT, MAIL_USE_TLS, MAIL_USERNAME, MAIL_PASSWORD — email settings for password reset

A `.flaskenv` file is included and sets `FLASK_APP=blog.py` for convenience.

## Initialize the Database

If you want to create or upgrade the database schema:

```bash
flask db upgrade
```

Note: This repository includes a pre-populated `app.db` for simple local use.

## Running the Application

Run the development server:

```bash
flask run
```

Open http://127.0.0.1:5000 in your browser.

## Example Accounts

See `user_login.md` for example credentials (useful if you're using the included `app.db`).

## Testing

Run the test script:

```bash
python test.py
```

## Project Structure (short)

- app/ — main application package (routes, models, forms, templates)
- migrations/ — database migrations
- blog.py — Flask app entry (used by flask CLI)
- config.py — application configuration
- app.db — included SQLite database (for local testing)
