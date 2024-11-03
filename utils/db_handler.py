import pymongo
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
try:
    client = pymongo.MongoClient(MONGO_URI)
    db = client['spill_the_tea_db']
    collection = db['tea_stories']
    print("Connected to MongoDB successfully.")
except pymongo.errors.ConnectionError as e:
    print(f"Failed to connect to MongoDB: {e}")

def save_tea_to_db(story, tags, drama_level):
    document = {
        "text": story,
        "tags": tags,
        "drama_level": drama_level,
        "timestamp": datetime.now()
    }
    try:
        result = collection.insert_one(document)
        print(f"Document inserted with id: {result.inserted_id}")
    except pymongo.errors.PyMongoError as e:
        print(f"failed to insert data: {e}")

def get_tea_from_db(search_query=""):
    if search_query:
        return list(collection.find({"tags": {"$in": search_query.split(",")}}))
    else:
        return list(collection.find())
