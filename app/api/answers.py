from flask import Blueprint, request, jsonify
from app.services.answer_service import save_answer

answers_bp = Blueprint("answers", __name__, url_prefix="/api/answers")

@answers_bp.route("", methods=["POST"])
def submit_answer():
    data = request.json
    save_answer(
        data["user_id"],
        data["question_id"],
        data["answer"]
    )
    return jsonify({"message": "Answer saved"})
