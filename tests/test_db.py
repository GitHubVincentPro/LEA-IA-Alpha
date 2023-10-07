```python
import unittest
from app.db import (
messages_collection,
create_message,
get_messages
)
from app.models import Message

class TestDatabase(unittest.TestCase):

def setUp(self):
messages_collection.delete_many({})

def test_create_message(self):

message = Message(texte="Bonjour", utilisateur="John")

message_id = create_message(message)

doc = messages_collection.find_one({"_id": message_id})
self.assertEqual(doc["texte"], "Bonjour")

def test_get_messages(self):

messages_collection.insert_many([
Message(**{"texte": "Hello", "utilisateur": "Jane"}).dict(),
Message(**{"texte": "Hi", "utilisateur": "Mike"}).dict()
])

messages = get_messages()

self.assertEqual(len(messages), 2)
self.assertEqual(messages[0].texte, "Hello")

def tearDown(self):
messages_collection.delete_many({})

if __name__ == '__main__':
unittest.main()
```