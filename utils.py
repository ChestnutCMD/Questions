import requests


def get_questions(count: int) -> list[dict]:
    """Функция запроса с публичного API вопросов для викторин, где count - количество запрашиваемых вопросов."""
    response = requests.get(f'https://jservice.io/api/random?count={count}').json()
    questions = []
    for quest in response:
        questions.append({'id_question': quest['id'],
                          'question': quest['question'],
                          'answer': quest['answer'],
                          'created_at': quest['created_at']})
    return questions
