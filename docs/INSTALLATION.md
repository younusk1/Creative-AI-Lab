# Installation

## Prerequisites

- Docker Desktop with Docker Compose enabled
- 16 GB RAM recommended
- At least 10 GB free disk space
- A terminal with Docker available on the path

## 1. Create local configuration

From the repository root:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace these placeholder values before starting services:

- `POSTGRES_PASSWORD`
- `WEBUI_SECRET_KEY`
- `N8N_ENCRYPTION_KEY`

Use long, unique values. The real `.env` file is intentionally ignored by Git.

## 2. Start the core stack

```powershell
docker compose up -d
docker compose ps
```

The first startup downloads container images and may take several minutes.

## 3. Pull the model

When the Ollama container is running:

```powershell
docker compose exec ollama ollama pull qwen2.5:3b
```

Check that it is available:

```powershell
docker compose exec ollama ollama list
```

## 4. Open the services

| Service | URL | Notes |
| --- | --- | --- |
| Open WebUI | http://localhost:3000 | Create the first local account here. |
| n8n | http://localhost:5678 | Create the owner account on first launch. |
| Adminer | http://localhost:8080 | Use server `postgres`, plus values from `.env`. |
| Ollama API | http://localhost:11434 | Local API endpoint. |

## Resource-saving commands

Stop only the services you are not using; data remains in Docker volumes.

```powershell
docker compose stop n8n adminer open-webui
docker compose start ollama open-webui
```

Stop the full stack:

```powershell
docker compose down
```

Do not use `docker compose down -v` unless you intentionally want to delete local databases, model downloads, users, and workflows.

## Optional Metabase

Metabase is not part of v0.1 to keep the default stack comfortable on 16 GB RAM. Add it later when the project has workflow data worth analyzing, and run it only for reporting or demos.
