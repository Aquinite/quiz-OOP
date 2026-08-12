import requests
import question_model

AMOUNT_OF_QUESTIONS = 10
TYPE_OF_QUESTIONS = "boolean"

QUIZ_PARAMETERS = {"amount":AMOUNT_OF_QUESTIONS,
                  "type": TYPE_OF_QUESTIONS}

def get_questions_from_api(api_parameters):
    questions_from_api = requests.get(url = "https://opentdb.com/api.php",
                                  params=api_parameters)
    questions_from_api.raise_for_status()

    pulled_questions = questions_from_api.json()
    question_data = pulled_questions.get("results")
    return question_data

def new_q_bank():
    question_data = get_questions_from_api(QUIZ_PARAMETERS)
    question_bank = [question_model.Question(question["question"], question["correct_answer"]) for question in question_data]

    return question_bank
