class Question:
    """This class allows questions in the question bank to become an object, with attributes such as the question itself and
     it's answer. Allows for easy access to the question itself."""
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
