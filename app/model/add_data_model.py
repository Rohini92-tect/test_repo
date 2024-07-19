from app.config.connection import MongoConnection

class AddData:
    _db = "Flask_project"
    @classmethod
    def add_data_into_collection(cls, data):
        client = MongoConnection.get_mongo_connection()
        db = client[cls._db]
        collection = db["new_data"]
        data = collection.insert_one(data)
        return str(data.inserted_id)
    
    @classmethod
    def get_data_for_csv(cls):
        try :
            client = MongoConnection.get_mongo_connection()
            db = client[cls._db]
            collection = db["new_data"]
            data = collection.find()
            if data:
                return list(data)
        except:
            print(Exception)
            