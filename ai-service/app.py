from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from services.groq_client import GroqClient
from middleware.sanitize import sanitize_input

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app)

groq_client = GroqClient()

@app.route("/describe", methods=["POST"])
@limiter.limit("30 per minute")
def describe():
    data = request.json
    text = sanitize_input(data.get("input"))

    if not text:
        return jsonify({"error": "Invalid or unsafe input"}), 400

    result = groq_client.generate_response(text)
    return jsonify({"response": result})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)