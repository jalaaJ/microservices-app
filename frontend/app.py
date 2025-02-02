from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Compose the backend URL from environment variables
backend_host = os.environ.get("BACKEND_HOST")
backend_port = os.environ.get("BACKEND_PORT")
BACKEND_URL = f"http://{backend_host}:{backend_port}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            requests.post(f"{BACKEND_URL}/add", json={"name": name})
    response = requests.get(f"{BACKEND_URL}/names")
    names = response.json() if response.status_code == 200 else []
    return render_template("index.html", names=names)

if __name__ == "__main__":
    
    frontend_host = os.environ.get("FRONTEND_HOST")
    frontend_port = int(os.environ.get("FRONTEND_PORT"))
    app.run(host=frontend_host, port=frontend_port)
