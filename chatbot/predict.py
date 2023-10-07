# chatbot/predict.py
from transformers import pipeline

nlp = pipeline("conversational")

def predict(message):
return nlp({'texte': message})[0]['texte']