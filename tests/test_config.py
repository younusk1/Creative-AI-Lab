import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from app.config import *

print("Project Root :", PROJECT_ROOT)
print("Docker Service :", DOCKER_SERVICE)
print("Model :", DEFAULT_MODEL)
print("Timeout :", REQUEST_TIMEOUT)
print("Log Directory :", LOG_DIR)