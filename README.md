# codex_test

Codexについて学習する為のリポジトリ

## Meal Prep Memo App

This repository now includes a small Django project named `mealprep`.
It allows you to track prepared food items and their expiration dates.

### Getting Started

1. Run the setup script
   ```bash
   ./setup.sh
   ```
   This will create a virtual environment, install dependencies and apply the
   initial database migrations.
2. Start the development server
   ```bash
   source venv/bin/activate
   python manage.py runserver 0.0.0.0:8000
   ```
3. Open your browser to `http://localhost:8000/` to use the app.

### Features
- Add, edit and delete prepared item memos
- Track preparation and expiration dates
