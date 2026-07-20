"""
config.py

Central configuration for the Creative AI Lab.

Purpose:
- Store application-wide constants.
- Avoid hardcoding values throughout the project.
- Provide a single location for future environment-variable support.
"""

from pathlib import Path

# ---------------------------------------------------------------------
# Project Paths
# ---------------------------------------------------------------------

# Project root (Creative-AI-Lab/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Logs
LOG_DIR = PROJECT_ROOT / "logs"

# Prompt templates (future use)
PROMPT_DIR = PROJECT_ROOT / "prompts"

# ---------------------------------------------------------------------
# Docker Configuration
# ---------------------------------------------------------------------

# Docker Compose service name
DOCKER_SERVICE = "ollama"

# ---------------------------------------------------------------------
# Local LLM Configuration
# ---------------------------------------------------------------------

DEFAULT_MODEL = "gemma2:2b"

# Future models
AVAILABLE_MODELS = {
    "gemma": "gemma2:2b",
    # "gemma_large": "gemma3:12b",
}

# ---------------------------------------------------------------------
# Execution Settings
# ---------------------------------------------------------------------

# Seconds before cancelling a model request
REQUEST_TIMEOUT = 120

# ---------------------------------------------------------------------
# Routing Settings (used later by the router)
# ---------------------------------------------------------------------

TOKEN_THRESHOLD = 4000

# ---------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------

LOG_LEVEL = "INFO"

# Create required directories automatically
LOG_DIR.mkdir(parents=True, exist_ok=True)
PROMPT_DIR.mkdir(parents=True, exist_ok=True)