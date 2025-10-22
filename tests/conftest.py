import os
import sys
import pytest

# Ensure project root is on sys.path so `app.py` can be imported as `app`
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import create_app


@pytest.fixture()
def app():
    # Configure app for testing
    os.environ.setdefault("SECRET_KEY", "test-secret")
    application = create_app()
    application.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False,
    )
    yield application


@pytest.fixture()
def client(app):
    return app.test_client()
