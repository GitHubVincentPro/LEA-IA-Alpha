# config/settings.py
import os

MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb://localhost:27017/chatbot")

BOT_MODEL = "chatbot/model"