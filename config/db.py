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
import certifi
import motor.motor_asyncio

# MongoDB Connection and Database
MONGO_URI = "mongodb+srv://ranvijay:ranvijay@cluster0.as3t4fm.mongodb.net/students"

# Create an event loop
loop = asyncio.get_event_loop()

# Create a Motor client
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI, tlsCAFile=certifi.where(), io_loop=loop)

# Access the database
db = client["students"]
collection = db["students"]
