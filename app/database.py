# Dans app/database.py

from pymongo import MongoClient
client = MongoClient(...)
db = client['chatbot']