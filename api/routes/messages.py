python
from fastapi import APIRouter, Body
from app.models import Message
from app.db import messages_collection

router = APIRouter()

@router.post("/")
async def create_message(message: Message = Body(...)):

# Validate message

result = await messages_collection.insert_one(message.dict())

# Handle possible errors

return {"message": "Message créé avec succès"}

@router.get("/")
async def get_messages():

messages = []

cursor = messages_collection.find()

for doc in await cursor.to_list(length=100):

message = Message(**doc)

# Validate message

messages.append(message)

return messages

@router.get("/{message_id}")
async def get_message(message_id: str):

document = await messages_collection.find_one({"_id": message_id})

if document:

message = Message(**document)

# Validate message

return message

return {"error": "Message non trouvé"}