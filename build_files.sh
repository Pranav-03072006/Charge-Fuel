#!/bin/bash
# This script runs automatically during Vercel's build phase
python manage.py migrate --no-input
python manage.py collectstatic --no-input
