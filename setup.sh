#!/usr/bin/env bash
# Simple setup script for Meal Prep Memo project
set -e

# Create virtual environment if it does not exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip and install Django and other requirements
pip install --upgrade pip
pip install django
pip install -r requirements.txt
# Run initial migrations

python mealprep/manage.py migrate
echo "Setup complete. Activate the environment with 'source venv/bin/activate'"
