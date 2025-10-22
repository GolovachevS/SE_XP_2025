from models import User


def test_password_hashing():
    u = User(email="test@example.com", name="Test User", role="student")
    u.set_password("secret123")
    assert u.check_password("secret123") is True
    assert u.check_password("wrong") is False
