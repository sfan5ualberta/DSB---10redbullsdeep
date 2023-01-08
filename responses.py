import random

def get_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return "What's up?"

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message[:11] == "createdeck ":
        return "create"

    if p_message[:11] == "deletedeck ":
        return "delete"

    if p_message[:11] == "browsedeck ":
        return "browse"

    if p_message[:8] == "addcard ":
        return "add"

    if p_message[:11] == "removecard ":
        return "remove"

    if p_message == "help":
        help_message = ("These are the currently available commands: \n"
                "\t !help: currently in use, showing all commands and their functionalities. \n"
                "\t !createDeck (Deck name): create a new deck to add cards to. \n"
                "\t !deleteDeck (Deck name): delete an existing deck.\n"
                "\t !browseDeck (Deck name): check all the cards in a deck \n"
                "\t !decks: list all deck names \n"
                "\t !addCard (Deck name) (Prompt) (Answer): add a card to a deck\n"
                "\t !removeCard (Deck name) (Card #): remove a card in the deck \n"
                "\t !review (Deck name): A random card is chosen in a deck, displaying its question.\n"
                "\t !flip: Flip the card, showing the answer to the current prompt."
                "\t !next: Show the next card. \n"
                "\t !stop: stop reviewing. Return to normal interface. \n"
        )
        return help_message
    
    return "I don't understand!"
