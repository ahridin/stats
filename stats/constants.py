"""Stats constants."""

# Standard Library
from pathlib import Path

CONFIG_DIR = Path("/etc/48ix-stats")
CONFIG_MAIN = CONFIG_DIR / "config.yaml"
DB_MAIN = CONFIG_DIR / "db-main.sqlite"

__version__ = "0.0.1"
