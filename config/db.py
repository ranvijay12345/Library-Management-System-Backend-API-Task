import certifi
from pymongo import MongoClient

# MongoDB Connection and Database
MONGO_URI = "mongodb+srv://ranvijay:ranvijay@cluster0.as3t4fm.mongodb.net/students"

client = MongoClient(MONGO_URI)

db = client["students"]
collection = db["students"]
