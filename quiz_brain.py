class QuizBrain:
    """This class is responsible for storing the question list of the quiz, displaying each question of the quiz,
     and calculating and displaying the score of the user.
     Has initial attributes: question number, questin list, and score"""
    def __init__(self,q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0

    def check_answer_and_score(self, user_answer, actual_answer):
        """Given parameter user_answer (the user's inputted answer) and actual_answer (from the question list passed into this class)
        , this function checks if the user answered correctly then updates the user's score based on the answer."""
        if user_answer.lower() == actual_answer.lower():
            self.score += 1
            print("You got it!")
        elif user_answer.lower() != actual_answer.lower():
            print("That's wrong. 😑")
        print(f"The correct answer is: {actual_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

    def next_question(self):
        """When ran, this function allows the program to display the current question and allows the user to input their answer."""
        new_question = self.q_list[self.question_number]
        self.question_number += 1 # We need to do this in order to call the new question when this function is called upon again.
        user_answer = input(f"Q.{self.question_number}:{new_question.text} (True/False?) ")
        self.check_answer_and_score(user_answer, new_question.answer) # runs the check answer and score function in order to
        #correctly update users score and give feedback to the user regarding their answer.
        print("\n")

    def still_has_questions(self):
        """Returns a boolean False or True in order for the while loop inside the main file to continue running the function "next_question".
        Stops when the question number equals the length of the question list passed to the class QuizBrain."""
        if self.question_number == (len(self.q_list)):
            return False
        else:
            return True
