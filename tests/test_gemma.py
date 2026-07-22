"""
tests/test_gemma.py

Integration test for the Gemma adapter.

Purpose:
    Verify that the application can communicate with
    the local Gemma model running inside Docker.

Run:
    python tests/test_gemma.py
"""

import sys
from pathlib import Path

# ---------------------------------------------------------
# Make project imports work when running this file directly.
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.models.gemma import Gemma, GemmaError

TEST_PROMPT = "Reply with exactly one word: success"


def check(message: str):
    """Print a successful checkpoint."""
    print(f"✓ {message}")


def main():

    print("=" * 60)
    print("Creative AI Lab")
    print("Gemma Adapter Integration Test")
    print("=" * 60)

    print()

    try:

        check("Imported Gemma adapter")

        gemma = Gemma()
        check("Created Gemma instance")

        print()
        print("Prompt")
        print("-" * 60)
        print(TEST_PROMPT)
        print("-" * 60)

        response = gemma.ask(TEST_PROMPT)

        check("Executed Docker command")
        check("Received model response")

        assert isinstance(response, str), "Response is not a string."
        assert response.strip(), "Response is empty."

        check("Validated response")

        print()
        print("Model Response")
        print("-" * 60)
        print(response)
        print("-" * 60)

        print()
        print("=" * 60)
        print("PASS")
        print("=" * 60)

    except AssertionError as error:

        print()
        print("❌ VALIDATION FAILED")
        print(error)
        sys.exit(1)

    except GemmaError as error:

        print()
        print("❌ GEMMA ADAPTER FAILED")
        print(error)
        sys.exit(1)

    except Exception as error:

        print()
        print("❌ UNEXPECTED ERROR")
        print(type(error).__name__)
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()