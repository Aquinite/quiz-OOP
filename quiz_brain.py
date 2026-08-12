import html
import data


class QuizBrain:
    """This class is responsible for storing the question list of the quiz, displaying each question of the quiz,
     and calculating and displaying the score of the user.
     Has initial attributes: question number, question list, current score, and the current question."""
    def __init__(self,q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0
        self.current_question = None

    def check_answer_and_score(self, user_answer):
        """Returns a boolean True or False depending on if the actual answer matches the user answer."""
        actual_answer = self.current_question.answer
        if user_answer.lower() == actual_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def next_question(self):
        """When ran, this function allows the program to display the current question and allows the user to input their answer."""
        self.current_question = self.q_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}:{question_text} (True/False?) "

    def still_has_questions(self):
        """Returns a boolean False or True in order for the while loop inside the main file to continue running the function "next_question".
        Stops when the question number equals the length of the question list passed to the class QuizBrain."""
        if self.question_number == (len(self.q_list)):
            return False
        else:
            return True

    def restart_quiz(self):
        """Resets your score and allows the UI to display the first question again."""
        self.score = 0
        self.question_number = 0
        self.current_question = None

    def new_quiz(self):
        self.q_list = data.new_q_bank()
        self.restart_quiz()

