import question_model
import data
import quiz_brain
import ui

question_bank = []

for question in data.question_data:
    transferred_question = question_model.Question(question["question"], question["correct_answer"])
    question_bank.append(transferred_question)

new_quiz = quiz_brain.QuizBrain(question_bank)
quiz_ui = ui.QuizUI(new_quiz)
