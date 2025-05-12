#!/bin/bash

# Stop on errors
set -e

echo "Starting deployment process..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run image optimization
echo "Optimizing images..."
python optimize_images.py

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Compress static files
echo "Compressing static files..."
python manage.py compress --force

# Apply migrations
echo "Applying migrations..."
python manage.py migrate

echo "Deployment completed successfully!"