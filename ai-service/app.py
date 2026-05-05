from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# -----------------------------
# HEALTH CHECK ENDPOINT
# -----------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "ai-service",
        "model": "groq"
    }), 200


# -----------------------------
# SAMPLE ROOT ENDPOINT
# -----------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI Service is running"
    })


# -----------------------------
# EXAMPLE AI ENDPOINT (if you already have Groq logic, keep yours)
# -----------------------------
@app.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input provided"}), 400

    input_text = data.get("text", "")

    return jsonify({
        "input": input_text,
        "output": "This is a placeholder AI response"
    })


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)