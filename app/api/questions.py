from flask import Blueprint, jsonify
from app.services.question_service import get_questions

questions_bp = Blueprint("questions", __name__, url_prefix="/api/questions")

@questions_bp.route("", methods=["GET"])
def list_questions():
    questions = get_questions()
    return jsonify([
        {"id": q.id, "text": q.text}
        for q in questions
    ])
