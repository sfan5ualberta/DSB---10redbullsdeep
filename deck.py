from card import Card
class Deck():
    def __init__(self, name, private):
        self.name = name
        self.cards = []
        self.private = private
    
    def addCard(self, question, answer):
        self.cards.append(Card(question, answer))
    
    def removeCard(self, cardNumber):
        if (len(self.card) <= cardNumber and cardNumber >= 0):
            self.card.pop(cardNumber)
        
