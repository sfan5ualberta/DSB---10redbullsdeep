import random
import pymongo
from pymongo import MongoClient


def get_response(message) -> str:
    mongo_url = "mongodb+srv://mongo:ilovemongodb@cluster0.jvcmb3x.mongodb.net/?retryWrites=true&w=majority"
    cluster = MongoClient(mongo_url)
    db = cluster["10redbullsdeep"]
    collection = db["Decks"]

    p_message = message.lower()

    if p_message == 'hello':
        return "What's up?"

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message[:11] == "createdeck ":
        deckname = p_message[11:]
        collection.insert_one({"name": deckname})
        return deckname, p_message, "create"

    if p_message[:11] == "deletedeck ":
        deckname = p_message[11:]
        collection.delete_one({"name": deckname})
        return "delete"

    if p_message[:11] == "browsedeck ":
        deckname = p_message[11:]
        return "browse"

    if p_message[:8] == "addcard ":
        deckname = p_message[8:]
        return "add"

    if p_message[:11] == "removecard ":
        deckname = p_message[11:]
        return "remove"

    if p_message[:5] == "review":
        deckname = p_message[5:]
        return "review"
    
    if p_message[:3] == "flip":
        return "review"
    
    if p_message[:3] == "next":
        return "review"

    if p_message[:3] == "stop":
        return "stop"
    
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
