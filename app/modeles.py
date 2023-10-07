# Dans modeles.py

from pydantic import BaseModel

class Message(BaseModel):
texte: str
utilisateur: str
