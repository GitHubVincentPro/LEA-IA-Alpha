```python
import json
from fastapi.testclient import TestClient

from api.main import app
from api.routes.messages import messages_collection
from app.models import Message

client = TestClient(app)

def test_create_message():

message = {"texte": "Bonjour", "utilisateur": "John"}

response = client.post("/messages", json=message)

assert response.status_code == 200
assert response.json()["message"] == "Message créé avec succès"

# Test en base
document = messages_collection.find_one({"texte": "Bonjour"})
assert document

def test_get_messages():

messages_collection.insert_many([
Message(**{"texte": "Salut", "utilisateur": "Jack"}).dict(),
Message(**{"texte": "Coucou", "utilisateur": "Jill"}).dict()
])

response = client.get("/messages")

assert response.status_code == 200
assert len(response.json()) == 2

def test_get_message():

message = Message(**{"texte": "Bonjour", "utilisateur": "John"})
_id = messages_collection.insert_one(message.dict()).inserted_id

response = client.get(f"/messages/{_id}")

assert response.status_code == 200
assert response.json()["texte"] == "Bonjour"
```