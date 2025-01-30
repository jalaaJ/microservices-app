from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
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
    app.run(host="127.0.0.1", port=5001)
