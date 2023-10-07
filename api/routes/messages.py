# Dans routes/messages.py

from .schemas import MessageSchema

@router.post("/")
async def create(message: MessageSchema):
...