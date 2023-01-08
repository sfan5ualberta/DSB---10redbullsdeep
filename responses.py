import random
import pymongo
from pymongo import MongoClient
from deck import Deck
from bson.binary import Binary
import pickle

def get_response(message) -> str:
    mongo_url = "mongodb+srv://mongo:ilovemongodb@cluster0.jvcmb3x.mongodb.net/?retryWrites=true&w=majority"
    cluster = MongoClient(mongo_url)
    db = cluster["10redbullsdeep"]
    collection = db["Decks"]

    p_message = message.lower()

    if p_message == 'hello':
        return "What's up?"


    if p_message[:11] == "createdeck ":
        deckname = p_message[11:]
        bytes = pickle.dumps(Deck(deckname))
        collection.insert_one({"name": deckname, "bin-data": Binary(bytes)})
        return f"Created deck: {deckname}"

    if p_message[:11] == "deletedeck ":
        deckname = p_message[11:]
        collection.delete_one({"name": deckname})
        return "delete"

    if p_message[:11] == "browsedeck ":
        deckname = p_message[11:]
        data = collection.find_one({"name": deckname},{"name":0, "_id": 0})
        deck = pickle.loads(data["bin-data"])
        return deck.showDeck()

        
    if p_message == "decks":
        # loop over all decks, printing their names
        deckStr = ""
        for doc in collection.find():
            deckStr += f'{doc["name"]}\n'
        return deckStr
    
    if p_message[:8] == "addcard ":
        split_message = p_message[8:].split(", ")
        if len(split_message) != 3:
            return "invalid input"
        deckname = split_message[0]
        prompt = split_message[1]
        answer = split_message[2]
        # get deck object with deckname from mongo
        data = collection.find_one({"name": deckname}, {"name":0, "_id":0})
        deck = pickle.loads(data["bin-data"])
        deck.addCard(prompt, answer)
        bytes = pickle.dumps(deck)
        collection.update_one({"name": deckname}, {"$set":{"bin-data": bytes}}, upsert = False)
        return f"Added {prompt}: {answer}"

    if p_message[:11] == "removecard ":
        split_message = p_message.split()
        if len(split_message) != 3:
            return "Invalid input"
        deckname = split_message[1]
        card_index = split_message[2]
        data = collection.find_one({"name": deckname},{"name":0, "_id": 0})
        deck = pickle.loads(data["bin-data"])
        deck.removeCard(card_index)
        bytes = pickle.dumps(deck)
        collection.update_one({"name": deckname}, {"$set":{"bin-data": bytes}}, upsert = False)
        return "Card has been removed"
    
    if p_message[:7] == "review ":
        deckname = p_message[7:]
        # get deck from mongo
        data = collection.find_one({"name": deckname}, {"name":0, "_id":0})
        deck = pickle.loads(data["bin-data"])
        str, deck = deck.review()
        bytes = pickle.dumps(deck)
        collection.update_one({"name": deckname}, {"$set":{"bin-data": bytes}}, upsert = False) 
        return str

    if p_message[:8] == "shuffle ":
        deckname = p_message[8:]
        data = collection.find_one({"name": deckname}, {"name":0, "_id":0})
        deck = pickle.loads(data["bin-data"])
        deck = deck.shuffle()
        bytes = pickle.dumps(deck)
        collection.update_one({"name": deckname}, {"$set":{"bin-data": bytes}}, upsert = False)
        return f"{deckname} is now shuffled!"

        
    if p_message == "pomodoro":
        pass # do nothing, handeled in bot.py
   
    if p_message == "help":
        help_message = ("These are the currently available commands: \n"
                "\t !addCard (Deck name), (Prompt), (Answer): add a card to a deck.\n"
                "\t !browseDeck (Deck name): check all the cards in a deck. \n"
                "\t !createDeck (Deck name): create a new deck to add cards to. \n"
                "\t !decks: list all deck names. \n"
                "\t !deleteDeck (Deck name): delete an existing deck.\n"
                "\t !help: currently in use, showing all commands and their functionalities. \n"
                "\t !removeCard (Deck name) (Card #): remove a card in the deck. \n"
                "\t !review (Deck name): display the next card in this deck.\n"
                "\t !shuffle (Deck name): randomizes the order of cards in this deck.\n")
        return help_message
    
    return "I don't understand! Check !help for legal commands."
