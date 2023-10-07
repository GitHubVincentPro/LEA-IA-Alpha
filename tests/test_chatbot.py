# tests/test_chatbot.py

from chatbot import predict

def test_predict():
response = predict("Bonjour")
assert response == "Salut ! Comment vas-tu ?"