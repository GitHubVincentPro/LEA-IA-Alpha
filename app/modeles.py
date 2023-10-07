# Dans app/models.py

from pydantic import BaseModel

class Message(BaseModel):
...


# Test de l'API

import requests

data = {"..."}
response = requests.post("http://localhost:8000/messages", json=data)