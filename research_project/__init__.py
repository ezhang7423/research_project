# type: ignore[attr-defined]
"""project_tag"""

""" 
Other global variables
"""
import sys
from importlib import metadata as importlib_metadata
from pathlib import Path

from eztils import abspath, setup_path, datestr

import os

from rich import print
from dotenv import load_dotenv
load_dotenv()


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
__version__ = version

REPO_DIR = setup_path(Path(abspath()) / "..")
DATA_ROOT = setup_path(os.getenv('DATA_ROOT') or  REPO_DIR / "data")
LOG_DIR = setup_path(DATA_ROOT / 'runs' / datestr())


print(f"LOG DIR: {LOG_DIR}")

if not (REPO_DIR / 'runs').exists():
    print(f'Creating symlink from {REPO_DIR / "runs"} to {LOG_DIR}')
    (REPO_DIR / 'runs').symlink_to(DATA_ROOT / 'runs')
