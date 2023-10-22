import logging
import os
import tempfile
from pathlib import Path
from typing import Iterator

import pytest

log = logging.getLogger(__name__)


@pytest.fixture
def temporary_home(monkeypatch: pytest.MonkeyPatch) -> Iterator[Path]:
    env_dir = os.getenv("TEST_TEMPORARY_DIR")
    if env_dir is not None:
        path = Path(env_dir).resolve()
        log.debug("Temp HOME directory: %s", str(path))
        monkeypatch.setenv("HOME", str(path))
        yield path
    else:
        log.debug("TEST_TEMPORARY_DIR not set, using TemporaryDirectory")
        with tempfile.TemporaryDirectory(prefix="pytest-") as dirpath:
            monkeypatch.setenv("HOME", str(dirpath))
            log.debug("Temp HOME directory: %s", str(dirpath))
            yield Path(dirpath)
