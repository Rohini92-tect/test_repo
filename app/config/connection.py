from pymongo import MongoClient

class MongoConnection:

    @classmethod
    def get_mongo_connection(cls):
        client = MongoClient("mongodb://localhost:27017/")
        return client