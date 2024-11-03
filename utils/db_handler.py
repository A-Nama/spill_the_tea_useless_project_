import pymongo
from datetime import datetime
import os

client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
db = client['spill_the_tea_db']
collection = db['tea_stories']

def save_tea_to_db(story, tags, drama_level):
    document = {
        "text": story,
        "tags": tags,
        "drama_level": drama_level,
        "timestamp": datetime.utcnow()
    }
    collection.insert_one(document)

def get_tea_from_db(search_query=""):
    if search_query:
        return list(collection.find({"tags": {"$in": search_query.split(",")}}))
    else:
        return list(collection.find())
