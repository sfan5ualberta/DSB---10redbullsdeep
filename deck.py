from card import Card
import random
class Deck():
    def __init__(self, name):
        self.name = name
        self.cards = []    

    def addCard(self, question, answer):
        self.cards.append(Card(question, answer))

    def removeCard(self, cardNumber):
        if (len(self.cards) >= int(cardNumber) and int(cardNumber) > 0):
            self.cards.pop(int(cardNumber)-1)

    def showDeck(self):
        ret_string = ""
        for i in range(0, len(self.cards)):
            ret_string += f"{i+1}: Q: {self.cards[i].getQuestion()} \nA: {self.cards[i].getAnswer()}\n"
        return ret_string

    def review(self):
        ret_string = f"{self.cards[0].getQuestion()}\n||{self.cards[0].getAnswer()}||"
        self.cards.append(self.cards.pop(0)) # move card to back
        return ret_string, self

    def shuffle(self):
        random.shuffle(self.cards)
        return self