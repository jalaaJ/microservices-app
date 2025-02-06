from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MongoDB Connection using environment variables
mongo_host = os.environ.get("MONGO_HOST")
mongo_port = os.environ.get("MONGO_PORT") 
client = MongoClient(f"mongodb://admin:password@{mongo_host}:{mongo_port}/?authSource=admin")
db = client.names_db
names_collection = db.names

@app.route("/add", methods=["POST"])
def add_name():
    data = request.json
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    names_collection.insert_one({"name": name})
    return jsonify({"message": "Name added successfully"}), 201

@app.route("/names", methods=["GET"])
def get_names():
    names = [doc["name"] for doc in names_collection.find()]
    return jsonify(names), 200

if __name__ == "__main__":
    # Use BACKEND_BIND_HOST for binding the Flask server
    backend_bind_host = os.environ.get("BACKEND_BIND_HOST", "0.0.0.0")
    backend_port = int(os.environ.get("BACKEND_PORT", 5001))
    app.run(host=backend_bind_host, port=backend_port)
