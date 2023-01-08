import random
from deck import Deck

def get_response(message, review) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return "What's up?"

    if p_message[:11] == "createdeck ":
        deckname = p_message[11:]
        # create empty deck object in mongodb with deckname
        return "create"

    if p_message[:11] == "deletedeck ":
        deckname = p_message[11:]
        #delete deck from mongodb
        return "delete"

    if p_message[:11] == "browsedeck ":
        deckname = p_message[11:]
        # get deck object with deckname from mongo
        Deck.showDeck()
        return "browse"
    
    if p_message == "decks":
        #loop over all decks, printing their names
        pass

    if p_message[:8] == "addcard ":
        split_message = p_message.split()
        if len(split_message) != 4:
            return "invalid input"
        deckname = split_message[1]
        prompt = split_message[2]
        answer = split_message[3]
        # get deck object with deckname from mongo
        Deck.addCard(prompt, answer)
        return "add"

    if p_message[:11] == "removecard ":
        split_message = p_message.split()
        if len(split_message) != 3:
            return "invalid input"
        deckname = split_message[1]
        card_index = split_message[2]
        Deck.removeCard(card_index)
        
        return "remove"
    
    if p_message[:7] == "review":
        deckname = p_message[7:]
        #get deck from mongo
        Deck.review()

    if p_message == "pomodoro":
        return ""

    if p_message == "help":
        help_message = ("These are the currently available commands: \n"
                "\t !help: currently in use, showing all commands and their functionalities. \n"
                "\t !createDeck (Deck name): create a new deck to add cards to. \n"
                "\t !deleteDeck (Deck name): delete an existing deck.\n"
                "\t !browseDeck (Deck name): check all the cards in a deck. \n"
                "\t !decks: list all deck names. \n"
                "\t !addCard (Deck name) (Prompt) (Answer): add a card to a deck.\n"
                "\t !removeCard (Deck name) (Card #): remove a card in the deck. \n"
                "\t !review (Deck name): Display the next card in this deck.\n"
        )
        return help_message
    
    return "I don't understand! Check !help for legal commands."
