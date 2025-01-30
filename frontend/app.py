from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5001"

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
    app.run(host="127.0.0.1", port=5000)
