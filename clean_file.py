import question_model
import data
import quiz_brain

question_bank = []


for question in data.question_data:
    transferred_question = question_model.Question(question["question"], question["correct_answer"])
    question_bank.append(transferred_question)

new_quiz = quiz_brain.QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()

print("You've completed the quiz!", f"Your final score is {new_quiz.score}/{new_quiz.question_number}.")