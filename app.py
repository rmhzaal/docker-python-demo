import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from inside a container!"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/info")
def info():
    # proves which container instance actually answered -- useful once
    # you're running more than one
    return jsonify({"app": "docker-python-demo", "hostname": os.uname().nodename})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
