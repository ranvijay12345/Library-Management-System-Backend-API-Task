# import certifi
# from pymongo import MongoClient
#
# # MongoDB Connection and Database
# MONGO_URI = "mongodb+srv://ranvijay:ranvijay@cluster0.as3t4fm.mongodb.net/students"
#
# client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
#
# db = client["students"]
# collection = db["students"]


import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB Connection and Database
MONGO_URI = "mongodb+srv://ranvijay:ranvijay@cluster0.as3t4fm.mongodb.net/students"

client = AsyncIOMotorClient(MONGO_URI)

# Access the database
db = client["students"]
collection = db["students"]
