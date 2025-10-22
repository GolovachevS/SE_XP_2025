from flask import Flask, render_template, redirect, url_for
from flask_login import current_user
from dotenv import load_dotenv
import os
from flask_migrate import Migrate, upgrade, migrate as migrate_db, init

from models import db, login_manager
from auth import auth_bp
from submissions import submissions_bp


load_dotenv()
migrator = Migrate()


def ensure_db_up_to_date(app):
    """Автоматически инициализирует и применяет миграции при запуске"""
    with app.app_context():
        if not os.path.exists("migrations"):
            print(">> [DB] initializing migrations")
            init()
            migrate_db(message="init")
            upgrade()
        else:
            try:
                migrate_db(message="auto")
                upgrade()
                print(">> [DB] migrations applied successfully")
            except Exception as e:
                print(">> [DB] migration failed:", e)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    migrator.init_app(app, db)

    app.register_blueprint(auth_bp)
    app.register_blueprint(submissions_bp)
    os.makedirs(app.config.get('UPLOAD_FOLDER', 'uploads'), exist_ok=True)

    @app.route('/')
    def index():
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        return render_template('dashboard.html')

    return app


app = create_app()


if __name__ == '__main__':
    ensure_db_up_to_date(app)
    app.run()
