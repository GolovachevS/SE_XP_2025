from urllib.parse import urlparse

from models import User, db


def test_register_creates_user_and_redirects_to_login(client, app):
    resp = client.post(
        "/register",
        data={
            "name": "Jane Doe",
            "email": "jane@example.com",
            "password": "secret123",
            "confirm": "secret123",
            "is_teacher": "y",
        },
        follow_redirects=False,
    )
    assert resp.status_code in (301, 302)
    assert urlparse(resp.headers.get("Location", "")).path.endswith("/login")

    with app.app_context():
        u = User.query.filter_by(email="jane@example.com").first()
        assert u is not None
        assert u.role == "teacher"


def test_register_duplicate_email_warns(client, app):
    with app.app_context():
        u = User(email="dup@example.com", name="Dup", role="student")
        u.set_password("secret123")
        db.session.add(u)
        db.session.commit()

    resp = client.post(
        "/register",
        data={
            "name": "Dup 2",
            "email": "dup@example.com",
            "password": "secret123",
            "confirm": "secret123",
        },
        follow_redirects=False,
    )
    assert resp.status_code in (301, 302)
    assert "/register" in resp.headers.get("Location", "")

    with app.app_context():
        assert User.query.filter_by(email="dup@example.com").count() == 1


def test_login_and_access_index(client, app):
    with app.app_context():
        u = User(email="login@example.com", name="Login User", role="student")
        u.set_password("secret123")
        db.session.add(u)
        db.session.commit()

    resp = client.post(
        "/login",
        data={"email": "login@example.com", "password": "secret123"},
        follow_redirects=False,
    )
    assert resp.status_code in (301, 302)

    resp2 = client.get("/")
    assert resp2.status_code == 200
    assert b"Email" not in resp2.data


def test_logout_requires_login_then_redirects(client, app):
    with app.app_context():
        u = User(email="out@example.com", name="Out User", role="student")
        u.set_password("secret123")
        db.session.add(u)
        db.session.commit()

    client.post(
        "/login",
        data={"email": "out@example.com", "password": "secret123"},
        follow_redirects=False,
    )

    resp = client.get("/logout", follow_redirects=False)
    assert resp.status_code in (301, 302)
    assert resp.headers.get("Location", "").endswith("/login")
