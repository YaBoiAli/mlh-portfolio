#!/bin/bash

# Navigate to the project directory
cd /root/mlh-portfolio

# Fetch the latest changes from the main branch and reset
git fetch && git reset origin/main --hard

# Spin down the Docker containers to prevent memory issues
docker compose -f docker-compose.prod.yml down

# Build and spin up the Docker containers
docker compose -f docker-compose.prod.yml up -d --build
