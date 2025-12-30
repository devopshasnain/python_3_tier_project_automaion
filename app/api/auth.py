from flask import Blueprint, request, jsonify
from app.services.auth_service import signup, login

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/signup", methods=["POST"])
def signup_route():
    data = request.json
    user = signup(data["email"], data["password"])
    if not user:
        return jsonify({"error": "User exists"}), 400
    return jsonify({"message": "Signup successful"})

@auth_bp.route("/login", methods=["POST"])
def login_route():
    data = request.json
    user = login(data["email"], data["password"])
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({"message": "Login successful", "user_id": user.id})
