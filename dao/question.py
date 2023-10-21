"""Data Access Object"""

from dao.model.question import Question


class QuestionDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, qid):
        return self.session.query(Question).get(qid)

    def get_all(self):
        return self.session.query(Question).all()

    def create(self, question_data):
        question = Question(**question_data)
        self.session.add(question)
        self.session.commit()
        return question

    def delete(self, qid):
        question = self.get_one(qid)
        self.session.delete(question)
        self.session.commit()
