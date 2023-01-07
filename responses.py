import random

def get_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return "What's up?"

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message[0:10] == 'createdeck ':
        print("create")
        pass
    if p_message[0:10] == 'deletedeck ':
        print("delete")
        pass
    if p_message[0:10] == 'browsedeck':
        print("browse")
        pass
    if p_message[0:8] == 'addcard':
        print("add")
        pass
    if p_message[0:10] == 'removecard':
        print("remove")
        pass
    if p_message == 'help':
        help_message = ("These are the currently available commands: \n"
                "\t !help: currently in use. \n"
                "\t !createDeck (Deck name): create a new deck to add cards to. \n"
                "\t !deleteDeck (Deck name): delete an existing deck.\n"
                "\t !browseDeck (Deck name): check all the cards in a deck \n"
                "\t !addCard (Deck name) (Prompt) (Answer): add a card to a deck\n"
                "\t !removeCard (Deck name) (Card #): remove a card in the deck \n"
        )
        return help_message
    
    return "I don't understand!"
