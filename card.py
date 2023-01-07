class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer 

    def displayQuestion(self):
        return self.question

    def displayAnswer(self):
        return self.answer
