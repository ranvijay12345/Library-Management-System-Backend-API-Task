import ssl

from pymongo import MongoClient
import certifi

# MongoDB Connection and Database
ca = certifi.where()
MONGO_URI = "mongodb+srv://ranvijay:ranvijay@cluster0.as3t4fm.mongodb.net/students"

client = MongoClient(MONGO_URI, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

db = client["students"]
collection = db["students"]
