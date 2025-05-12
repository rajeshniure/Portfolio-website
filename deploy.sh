#!/bin/bash

# Stop on errors
set -e

echo "Starting deployment process..."

# Set production settings
export DJANGO_SETTINGS_MODULE=django_project.settings_production

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run image optimization
echo "Optimizing images..."
python optimize_images.py

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Disable compress for production
echo "Skipping compression for production..."
# python manage.py compress --force  # Commented out to avoid django-compressor issues

# Apply migrations
echo "Applying migrations..."
python manage.py migrate

echo "Deployment completed successfully!"