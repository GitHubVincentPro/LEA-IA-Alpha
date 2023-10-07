# Dans routes/utilisateurs.py

from fastapi import APIRouter, Body
from app.models import Utilisateur
from app.db import utilisateurs

router = APIRouter()

@router.post("/")
def create_user(user: Utilisateur):
user.date_creation = format_date(datetime.now())
return utilisateurs.insert_one(user.dict())