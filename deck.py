class Deck():
    def __init__(self, name, private):
        self.name = name
        self.card = []
        self.private = private
    
    def addCard(self, question, answer):
        card.append(Card(question, answer))
    
    def removeCard(self, cardNumber):
        if (len(self.card) <= cardNumber and cardNumber >= 0):
            card.pop(cardNumber)
        
