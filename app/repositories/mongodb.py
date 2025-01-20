from pymongo import MongoClient
from app.config import Config

client = MongoClient(Config.MONGO_URI)
db = client["requirements"]
collection = db["generated_requirements"]

def save_to_mongodb(idea: str, requirements: str):
    data = {"idea": idea, "requirements": requirements}
    collection.insert_one(data)
