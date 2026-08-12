import data
import quiz_brain
import ui


question_bank = data.new_q_bank()
new_quiz = quiz_brain.QuizBrain(question_bank)
quiz_ui = ui.QuizUI(new_quiz)
