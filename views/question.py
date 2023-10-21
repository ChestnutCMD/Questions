from flask_restx import Namespace, Resource, fields
from flask import request

from dao.model.question import QuestionSchema
from implemented import question_service
from utils import get_questions

questions_ns = Namespace('questions')

# Модель для swagger
questions_model = questions_ns.model('questions', {
    "questions_num": fields.Integer(required=True, description='Количество вопросов')})


@questions_ns.route('/')
class QuestionsView(Resource):
    def get(self) -> tuple[list, int]:
        """Получение всех вопросов из БД"""
        all_questions: list = question_service.get_all()
        result = QuestionSchema(many=True).dump(all_questions)
        return result, 200

    @questions_ns.expect(questions_model)
    def post(self) -> tuple[list, int]:
        """Тестовое задание.
        Запрашивает с публичного API (англоязычные вопросы для викторин)
        https://jservice.io/api/random?count=1
        указанное в полученном запросе количество вопросов и сохраняет их в БД"""

        all_question: list = question_service.get_all()
        try:
            result = QuestionSchema().dump(all_question[-1])
        except IndexError:
            result = None

        # Генератор списка list_id из вопросов находящихся в БД
        list_id = [i.id_question for i in all_question]

        count_questions: int = request.json["questions_num"]
        questions_list: list = get_questions(count_questions)

        for question_data in questions_list:
            # В случае, если в БД имеется такой же вопрос, к публичному API с викторинами
            # выполняются дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
            # Список list_id нужен, чтобы не делать много запросов в бд, но есть нюанс...
            while question_data['id_question'] in list_id:
                question_data: dict = get_questions(1)[0]
            question_service.create(question_data)

        return result, 201  # Возвращает предыдущий сохранённый вопрос для викторины.


@questions_ns.route('/<qid>')
class QuestionView(Resource):
    def get(self, qid: int) -> tuple[dict, int]:
        """Получение вопроса из БД по id"""
        question: dict = question_service.get_one(qid)
        result: dict = QuestionSchema().dump(question)
        return result, 200

    def delete(self, qid: int) -> tuple[str, int]:
        """Удаление вопроса из БД"""
        question_service.delete(qid)
        return '', 204
