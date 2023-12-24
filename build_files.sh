#!/bin/bash

# Build the project
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

apt-get update
apt-get install -y libpq-dev

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear