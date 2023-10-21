"""business logic"""

from dao.question import QuestionDAO


class QuestionService:
    def __init__(self, dao: QuestionDAO):
        self.dao = dao

    def get_one(self, qid):
        return self.dao.get_one(qid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, question_data):
        return self.dao.create(question_data)

    def delete(self, qid):
        self.dao.delete(qid)
