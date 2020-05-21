import pymongo
import os
from typing import Dict

class Database:
    # for heroku
    URI = os.environ.get("MONGODB_URI")
    DATABASE = pymongo.MongoClient(URI).get_default_database() # free tier in herku can't create a new database
    
    # for local database
    # URI = "mongodb://127.0.0.1:27017/pricing" # pricing: name of database
    # DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        return Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> None:
        return Database.DATABASE[collection].remove(query)


