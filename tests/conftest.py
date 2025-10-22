import os
import sys
import pytest

# Ensure project root is on sys.path so `app.py` can be imported as `app`
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app import create_app  # noqa: E402
from models import db  # noqa: E402


@pytest.fixture()
def app(tmp_path):
    # Configure app for testing
    os.environ.setdefault("SECRET_KEY", "test-secret")
    application = create_app()
    application.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        UPLOAD_FOLDER=str(tmp_path),
    )
    with application.app_context():
        db.create_all()
    yield application
    with application.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()
