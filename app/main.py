from flask import Flask
from app.db.database import db
from app.api.auth import auth_bp
from app.api.questions import questions_bp
from app.api.answers import answers_bp
from sqlalchemy import text
import os
import sys


def create_app():
    app = Flask(__name__)

    # 🔐 DATABASE CONFIG (ENV BASED)
    db_user = os.getenv("DB_USER", "root")
    db_password = os.getenv("DB_PASSWORD", "root")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "devops_db")

    # ✅ IMPORTANT: MySQL DATABASE URI
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ✅ ROOT ROUTE
    @app.route("/")
    def root():
        return {
            "status": "ok",
            "message": "Backend is running 🚀"
        }

    # 🔌 INIT DB
    db.init_app(app)

    # 🔗 REGISTER ROUTES
    app.register_blueprint(auth_bp)
    app.register_blueprint(questions_bp)
    app.register_blueprint(answers_bp)

    # 🧪 TEST DB CONNECTION (FAIL FAST)
    with app.app_context():
        try:
            db.session.execute(text("SELECT 1"))
            print("✅ Database connected successfully")
            db.create_all()
        except Exception as e:
            print("❌ Database connection failed")
            print(e)
            sys.exit(1)  # 🔥 HARD STOP — app will NOT start

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
