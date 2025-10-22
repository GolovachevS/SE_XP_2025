import app as app_module


def test_ensure_db_up_to_date_initializes_when_no_migrations(app, monkeypatch, tmp_path):
    calls = {"init": 0, "migrate": 0, "upgrade": 0}

    def fake_exists(path):
        return False

    def fake_init():
        calls["init"] += 1

    def fake_migrate(message=None):
        calls["migrate"] += 1

    def fake_upgrade():
        calls["upgrade"] += 1

    monkeypatch.setattr(app_module.os.path, "exists", fake_exists)
    monkeypatch.setattr(app_module, "init", fake_init)
    monkeypatch.setattr(app_module, "migrate_db", fake_migrate)
    monkeypatch.setattr(app_module, "upgrade", fake_upgrade)

    app_module.ensure_db_up_to_date(app)
    assert calls == {"init": 1, "migrate": 1, "upgrade": 1}


def test_ensure_db_up_to_date_runs_migrate_and_upgrade_when_migrations_exist(app, monkeypatch):
    calls = {"init": 0, "migrate": 0, "upgrade": 0}

    def fake_exists(path):
        return True

    def fake_init():
        calls["init"] += 1

    def fake_migrate(message=None):
        calls["migrate"] += 1

    def fake_upgrade():
        calls["upgrade"] += 1

    monkeypatch.setattr(app_module.os.path, "exists", fake_exists)
    monkeypatch.setattr(app_module, "init", fake_init)
    monkeypatch.setattr(app_module, "migrate_db", fake_migrate)
    monkeypatch.setattr(app_module, "upgrade", fake_upgrade)

    app_module.ensure_db_up_to_date(app)
    assert calls == {"init": 0, "migrate": 1, "upgrade": 1}
