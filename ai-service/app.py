from flask import Flask, request, jsonify
from services.groq_client import get_ai_response

app = Flask(__name__)


# -------------------
# CHAT ENDPOINT
# -------------------
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not data or "prompt" not in data:
        return jsonify({"error": "prompt is required"}), 400

    if data["prompt"] is None:
        return jsonify({"error": "prompt cannot be null"}), 400

    try:
        result = get_ai_response(data["prompt"])
        return jsonify(result), 200

    except Exception:
        return jsonify({"error": "internal error"}), 500


# -------------------
# DESCRIBE ENDPOINT
# -------------------
@app.route("/describe", methods=["POST"])
def describe():
    data = request.get_json(silent=True)

    if not data or "input" not in data:
        return jsonify({"error": "input required"}), 400

    try:
        result = get_ai_response(data["input"])
        return jsonify({"description": result["response"]}), 200

    except Exception:
        return jsonify({"error": "internal error"}), 500


# -------------------
# RUN APP
# -------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)