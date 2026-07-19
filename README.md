# Project 01: Flask + PostgreSQL + Nginx

A 3-tier containerized web application demonstrating core DevOps practices.

## Architecture

```
Browser → Nginx (80) → Flask (5000) → PostgreSQL (5432)
  Proxy      Web App        Database
```

## Quick Start

```bash
# Clone the repo
git clone https://github.com/zeroxin2003/project-01-flask-docker.git
cd project-01-flask-docker

# Start all services
docker compose up -d --build

# Visit http://localhost
```

## What's Included

| Component | Tech | Purpose |
|-----------|------|---------|
| Reverse Proxy | Nginx Alpine | SSL termination, load balancing ready |
| Web App | Flask 3.1 + Python 3.12 | Application logic |
| Database | PostgreSQL 16 Alpine | Persistent data storage |
| Orchestration | Docker Compose | Multi-container management |

## Key Features

- **Health checks** on all 3 services with proper startup ordering
- **Persistent data** via named Docker volume (`db_data`)
- **Nginx reverse proxy** hides internal Flask port from external access
- **Environment variables** for database configuration (no hardcoded secrets)
- **Layer-optimized Dockerfile** (requirements.txt copied before code for cache efficiency)

## Useful Commands

```bash
# Start services
docker compose up -d --build

# Check service status and health
docker compose ps

# View logs
docker compose logs -f

# Stop and remove containers (data preserved)
docker compose down

# Stop and remove containers + data
docker compose down -v

# Restart a single service
docker compose restart web
```

## DevOps Concepts Demonstrated

1. **Containerization** — Each service runs in its own isolated container
2. **Docker Compose networking** — Services communicate by service name
3. **Volume persistence** — Database survives container restarts
4. **Reverse proxy pattern** — Nginx as single entry point
5. **Health checks** — `depends_on` with `condition: service_healthy` ensures correct startup order
6. **Layer caching** — Dockerfile copies `requirements.txt` before source code
7. **Environment-based config** — Database credentials via environment variables

## Project Structure

```
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Flask container build
├── docker-compose.yml      # Multi-service orchestration
├── nginx/
│   └── default.conf        # Nginx reverse proxy config
├── .dockerignore
└── .gitignore
```
