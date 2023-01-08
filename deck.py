from card import Card
import random
class Deck():
    def __init__(self, name):
        self.name = name
        self.cards = []    
    def addCard(self, question, answer):
        self.cards.append(Card(question, answer))
    
    def removeCard(self, cardNumber):
        if (len(self.cards) <= cardNumber and cardNumber >= 0):
            self.cards.pop(cardNumber)
            
    def showDeck(self):
        for i in range(0, len(self.cards)):
            print("%d : " % i, end='')
            print(self.cards[i])

    def review(self):
        print(self.cards[0])
        self.cards.append(self.cards.pop(self.curCard)) # move card to back

    def shuffle(self):
        random.shuffle(self.cards)