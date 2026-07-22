"""
app/models/base.py

Abstract base class for all language models used in Creative AI Lab.

Every model implementation must provide an ask() method that accepts
a prompt and returns the model response.
"""

from abc import ABC, abstractmethod


class BaseModel(ABC):
    """Base interface for all LLM implementations."""

    @abstractmethod
    def ask(self, prompt: str) -> str:
        """
        Send a prompt to the model.

        Parameters
        ----------
        prompt : str

        Returns
        -------
        str
            Model response.
        """
        pass