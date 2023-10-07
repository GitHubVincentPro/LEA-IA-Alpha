# tests/test_api.py

import requests

from app.models import Message

def test_create_message():
message = Message(texte="Bonjour", utilisateur="John")
response = requests.post("http://localhost:8000/messages", json=message.dict())
assert response.status_code == 200