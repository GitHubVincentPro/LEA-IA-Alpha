# Dans routes/messages.py

from fastapi import APIRouter
from app.models import Message
from app.db import messages

router = APIRouter()

@router.post("/")
async def create_message(message: Message):
return await messages.insert_one(message.dict())