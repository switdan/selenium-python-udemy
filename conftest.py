import os
import webbrowser
from pathlib import Path


def pytest_sessionfinish(session, exitstatus):
    report_path = Path("reports/report.html")

    if report_path.exists():
        webbrowser.open(report_path.resolve().as_uri())