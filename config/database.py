from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:test%40123@cosmoclouddb.jlhyqzp.mongodb.net/?retryWrites=true&w=majority&appName=cosmoCloudDB")
db  = client.root_db

collection_name = db["root_collection"]