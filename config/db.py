from pymongo import MongoClient

# MongoDB Connection and Database
tls = True
tlsAllowInvalidCertificates = True
MONGO_URI = "mongodb+srv://ranvijay:ranvijay@cluster0.as3t4fm.mongodb.net/students"

client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)

db = client["students"]
collection = db["students"]
