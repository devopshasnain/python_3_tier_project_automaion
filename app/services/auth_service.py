from app.models.user import User
from app.db.database import db
from app.utils.password import hash_password, verify_password

def signup(email, password):
    if User.query.filter_by(email=email).first():
        return None

    user = User(
        email=email,
        password_hash=hash_password(password)
    )
    db.session.add(user)
    db.session.commit()
    return user

def login(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user
