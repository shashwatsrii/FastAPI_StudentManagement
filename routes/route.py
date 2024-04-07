from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId
from pydantic import BaseModel

router = APIRouter()

#GET Request
@router.get("/")
async def get_root():
    '''Return the name'''
    todos = list_serial(collection_name.find())
    return todos

@router.post("/")
async def post_root(todo : Todo):
    collection_name.insert_one(dict(todo))
