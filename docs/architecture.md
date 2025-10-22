# Nuthouse Studios System Architecture

## Overview
This project is built to manage content and data via a Master Controller Agent (MCA) that automates database maintenance and content deployment.

## Folder Structure
- `/content` → Site content and static files
- `/src` → Python source code (controller agent, server, config)
- `/docs` → Documentation
- `/.github/workflows` → CI/CD automation

## MCA Workflow
1. Agent initializes and loads `settings.json`.
2. DatabaseManager handles syncing and updates.
3. Flask server serves content and exposes API endpoints.
4. CI/CD workflows or Dockerfile handle deployment.

## Deployment Options
- Heroku via Dockerfile
- Local Flask server for development
- GitHub Pages for static HTML content
