# Dans bd.py

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
bd = client["chatbot"]
messages = bd["messages"]