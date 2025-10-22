from flask import Response


def test_index_redirects_anonymous(client):
    resp: Response = client.get("/", follow_redirects=False)
    assert resp.status_code in (301, 302)
    # Should redirect to login page for anonymous users
    assert resp.headers.get("Location", "").endswith("/login")


def test_login_page_renders(client):
    resp: Response = client.get("/login")
    assert resp.status_code == 200
    assert b"Email" in resp.data
