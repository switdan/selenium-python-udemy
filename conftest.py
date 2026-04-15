import os
import time
from pathlib import Path

MAX_WAIT_SECONDS = 10
CHECK_INTERVAL = 0.5


def pytest_unconfigure(config):
    if hasattr(config, "workerinput"):
        return

    report_path = config.getoption("htmlpath")
    if not report_path:
        return

    path = Path(report_path).resolve()

    timeout = time.time() + MAX_WAIT_SECONDS

    while time.time() < timeout:
        if path.exists():
            os.startfile(path)
            return
        time.sleep(CHECK_INTERVAL)