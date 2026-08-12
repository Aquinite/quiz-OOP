import tkinter as tk
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        #Window for UI
        self.window = tk.Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        #Score label
        self.score_label = tk.Label(text = f"Score: {self.quiz.score}/{len(self.quiz.q_list)}",
                                    font=("Arial", 12), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=2)

        #Canvas in the middle of the screen with text showing the text of question
        self.canvas = tk.Canvas(self.window, bg="white", width = 500, height = 350,highlightthickness=0)
        self.question_text = self.canvas.create_text(250, 175, text = "", font=("Arial", 20, "italic"), width = 480, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=3, padx=20, pady=20)

        #PhotoImage for buttons
        true_image = tk.PhotoImage(file="images/true.png")
        false_image = tk.PhotoImage(file="images/false.png")

        #Buttons at the bottom of the screen
        self.true_button = tk.Button(image=true_image, highlightthickness=0,
                                     highlightbackground=THEME_COLOR, bg=THEME_COLOR,command = self.true_pressed,activebackground="black")
        self.true_button.grid(row=2, column=0)

        self.false_button = tk.Button(image=false_image, highlightthickness=0,
                                      highlightbackground=THEME_COLOR, bg=THEME_COLOR, command = self.false_pressed,activebackground="black")
        self.false_button.grid(row=2, column=2)
        
        self.restart_button = tk.Button(text = "Restart Quiz", highlightthickness=0,
                                      highlightbackground=THEME_COLOR, bg=THEME_COLOR, command = self.ui_reset_quiz,activebackground="black")
        self.restart_button.grid(row=0, column=0)

        self.new_quiz_button = tk.Button(text="Start New Quiz", highlightthickness=0,
                                      highlightbackground=THEME_COLOR, bg=THEME_COLOR, command=self.start_new_quiz, activebackground="black")
        self.new_quiz_button.grid(row=0, column=1)

        self.show_next_question()

        #Mainloop for window UI
        self.window.mainloop()

    def show_next_question(self):
        """Displays the next question into the canvas as text."""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.q_list)}")
            shown_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = shown_text, fill=THEME_COLOR)
        else:
            self.true_button.config(state="disabled") #removes the button press from these buttons
            self.false_button.config(state="disabled")
            self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of this quiz.", fill=THEME_COLOR)
            messagebox.showinfo(message = f"Your final score is: {self.quiz.score}/{len(self.quiz.q_list)}")

    def screen_feedback(self,is_right):
        """Depending on your answer, displays the appropriate feedback on the screen."""
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, text="Correct!", fill= "white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, text="Incorrect!", fill= "white")
        self.window.after(1000, self.show_next_question)

    def true_pressed(self):
        """Passes True as the answer in order to run the check answer function from quiz_brain."""
        is_right = self.quiz.check_answer_and_score("True")
        self.screen_feedback(is_right)

    def false_pressed(self):
        """Passes False as the answer in order to run the check answer function from quiz_brain."""
        is_right = self.quiz.check_answer_and_score("False")
        self.screen_feedback(is_right)

    def ui_restart_quiz(self):
        """Resets your score, and starts you at question 1 of the current quiz."""
        user_response = messagebox.askokcancel(title="Restart Quiz",
                                               message="This will restart the current quiz. Do you wish to continue?")
        if user_response:
            self.quiz.restart_quiz()
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
            self.show_next_question()

    def start_new_quiz(self):
        """Pulls a new set of 10 questions from the quiz API for you to play through."""
        user_response = messagebox.askokcancel(title="Start New Quiz",
                               message="This will start a new quiz with a new set of questions. Do you wish to continue?")
        if user_response:
            self.quiz.new_quiz()
            self.quiz.restart_quiz()
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
            self.show_next_question()












