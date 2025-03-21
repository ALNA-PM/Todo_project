# filepath: /c:/Users/ACER/Desktop/Todo_jan18/Backend/todo/mongo.py
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['todo_db']
todos_collection = db['todos']