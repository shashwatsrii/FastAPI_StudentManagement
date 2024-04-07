from pymongo import MongoClient
from dotenv import load_dotenv
import os


load_dotenv()
database_url = os.getenv("DATABASE_URL")

client = MongoClient(database_url)
db  = client.root_db

collection_name = db["root_collection"]