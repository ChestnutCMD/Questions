"""dependencies"""
from dao.question import QuestionDAO
from service.question import QuestionService
from setup_db import db

question_dao = QuestionDAO(session=db.session)
question_service = QuestionService(dao=question_dao)
