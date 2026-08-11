import requests


AMOUNT_OF_QUESTIONS = 10
TYPE_OF_QUESTIONS = "boolean"

api_parameters = {"amount":AMOUNT_OF_QUESTIONS,
                  "type": TYPE_OF_QUESTIONS}
questions_from_api = requests.get(url = "https://opentdb.com/api.php",
                                  params=api_parameters)
questions_from_api.raise_for_status()

pulled_questions = questions_from_api.json()
question_data = pulled_questions.get("results")
