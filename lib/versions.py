# lib/versions.py
import sys
import requests # type: ignore
import pytest # type: ignore

def python_version():
    return sys.version_info

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__
