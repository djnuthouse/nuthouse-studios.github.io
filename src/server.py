from flask import Flask, send_from_directory, request, jsonify
from agent.controller import MasterController
import os

app = Flask(__name__, static_folder="../content", static_url_path="")
controller = MasterController()

@app.route("/")
def index():
    return send_from_directory("../content", "index.html")

@app.route("/api/update", methods=["POST"])
def update_data():
    data = request.json or {}
    controller.db.sync()  # simulate system update
    return jsonify({"status": "success", "received": data})

@app.route("/api/status")
def status():
    return jsonify({"system": "Nuthouse Studios", "state": "online"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Server running on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port)
