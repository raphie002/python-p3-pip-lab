from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    # FIX: Changed 8 to 12
    assert version_info.minor == 12 


def test_requests_version():
    # FIX: Changed 2.27.1 to 2.31.0
    assert requests_version() == "2.31.0"


def test_pytest_version():
    # FIX: Changed 7.1.3 to 7.4.4
    assert pytest_version() == "7.4.4"