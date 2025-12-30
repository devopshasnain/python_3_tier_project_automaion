from app.models.answer import Answer
from app.db.database import db

def save_answer(user_id, question_id, answer_text):
    answer = Answer(
        user_id=user_id,
        question_id=question_id,
        answer=answer_text
    )
    db.session.add(answer)
    db.session.commit()
