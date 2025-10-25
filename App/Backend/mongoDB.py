from pymongo import MongoClient

mongo_client = MongoClient("mongodb://admin:admin123@localhost:27017/")

db_access = mongo_client["ic-ia"]

collection_access = db_access["vector-store"]

new_object = {
    '_id': 1,
    'name': 'Matheus',
    'age': 30,
    'city': 'Cuiabá'
}

#collection_access.insert_one(new_object)

print(collection_access.find_one({'id': 1}))
