python
from pydantic import BaseModel, validator

class Message(BaseModel):

texte: str
utilisateur: str

@validator("texte")
def texte_length_check(cls, v):
if len(v) < 5:
raise ValueError("Le texte doit faire plus de 5 caractères")

@validator("utilisateur")
def utilisateur_check(cls, v):
if len(v) < 3:
raise ValueError("L'utilisateur doit faire plus de 3 caractères")

async def validate_message(message: Message):

try:
message.dict()
except ValidationError as e:
raise ValueError("Message invalide") from e

return message