from app.models.question import Question

def get_questions():
    return Question.query.all()
