"""
app/models/gemma.py

Gemma interface for Creative AI Lab.

Responsibilities:
- Send prompts to Gemma running inside the Ollama Docker container.
- Return the model response.
- Raise clear exceptions when execution fails.

This module intentionally knows nothing about routing, logging,
or other models.
"""

from __future__ import annotations

import subprocess

from app.config import DEFAULT_MODEL, DOCKER_SERVICE, REQUEST_TIMEOUT


class GemmaError(Exception):
    """Raised when Gemma execution fails."""


class Gemma:
    """Simple interface for interacting with the local Gemma model."""

    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        service: str = DOCKER_SERVICE,
        timeout: int = REQUEST_TIMEOUT,
    ):
        self.model = model
        self.service = service
        self.timeout = timeout

    def ask(self, prompt: str) -> str:
        """
        Send a prompt to Gemma and return the response.

        Parameters
        ----------
        prompt : str
            The prompt to send to the model.

        Returns
        -------
        str
            The model's response.

        Raises
        ------
        ValueError
            If the prompt is empty.

        GemmaError
            If Docker or Ollama returns an error.
        """

        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        command = [
            "docker",
            "compose",
            "exec",
            "-T",
            self.service,
            "ollama",
            "run",
            self.model,
            prompt,
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )

        except subprocess.TimeoutExpired as exc:
            raise GemmaError(
                f"Request timed out after {self.timeout} seconds."
            ) from exc

        except FileNotFoundError as exc:
            raise GemmaError(
                "Docker is not installed or is not available in PATH."
            ) from exc

        if result.returncode != 0:
            raise GemmaError(
                f"""
Gemma execution failed.

Exit Code:
{result.returncode}

STDERR:
{result.stderr.strip()}
"""
            )

        return result.stdout.strip()