from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, USER, PASS):
        # MongoDB Connection Variables
        USER = 'root'
        PASS = 'x1vXfXIAAm'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 33914
        DB = 'AAC'
        COL = 'animals'

        # Establish connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert a new document into the collection"""
        if data:
            insert = self.database.animals.insert_one(data)
            return bool(insert.inserted_id)
        raise Exception("Nothing to create, because data parameter is empty")

    def read(self, read=None):
    if read is None:
        read = {}
    return list(self.database.animals.find(read, {"_id": False}))


    def update(self, data, updateData):
        """Update documents in the collection"""
        if data:
            update_result = self.database.animals.update_many(data, {"$set": updateData})
            return update_result.raw_result
        raise Exception("Nothing to update, because data parameter is empty")

    def delete(self, deleteData):
        """Delete documents from the collection"""
        if deleteData:
            delete_result = self.database.animals.delete_many(deleteData)
            return delete_result.raw_result
        raise Exception("Nothing to delete, because data parameter is empty.")
