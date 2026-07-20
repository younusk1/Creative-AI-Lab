"""
tests/test_gemma.py

Integration test for the Gemma interface.

Purpose:
    Verify that the application can communicate with
    the local Gemma model running in Docker.

Run:
    python tests/test_gemma.py
"""

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.models.gemma import Gemma, GemmaError


TEST_PROMPT = "Reply with exactly one word: success"


def main():

    print("=" * 60)
    print("Creative AI Lab")
    print("Gemma Integration Test")
    print("=" * 60)

    print(f"\nPrompt:\n{TEST_PROMPT}\n")

    gemma = Gemma()

    try:
        response = gemma.ask(TEST_PROMPT)

        print("-" * 60)
        print("Model Response:")
        print(response)
        print("-" * 60)

        print("\n✅ Test Passed")
        print("Successfully communicated with Gemma.")

    except GemmaError as error:

        print("\n❌ Test Failed")
        print(error)
        sys.exit(1)

    except Exception as error:

        print("\n❌ Unexpected Error")
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()