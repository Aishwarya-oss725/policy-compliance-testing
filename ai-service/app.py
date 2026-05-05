from flask import Flask, request, jsonify

app = Flask(__name__)

# -----------------------------
# HEALTH CHECK (optional but useful)
# -----------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "AI Service Running"})


# -----------------------------
# DESCRIBE ENDPOINT
# -----------------------------
@app.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()
    user_input = data.get("input", "")

    return jsonify({
        "description": f"Mock response for: {user_input}"
    })


# -----------------------------
# RECOMMEND ENDPOINT
# -----------------------------
@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    user_input = data.get("input", "")

    return jsonify({
        "recommendations": [
            {
                "action_type": "improve",
                "description": f"Enhance security for: {user_input}",
                "priority": "high"
            },
            {
                "action_type": "monitor",
                "description": "Enable logging and alerts",
                "priority": "medium"
            },
            {
                "action_type": "prevent",
                "description": "Add rate limiting and validation",
                "priority": "high"
            }
        ]
    })


# -----------------------------
# GENERATE REPORT ENDPOINT
# -----------------------------
@app.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()
    user_input = data.get("input", "")

    return jsonify({
        "title": "AI Generated Report",
        "summary": f"Analysis performed on: {user_input}",
        "overview": "System is operating within expected parameters.",
        "key_items": [
            "Security checks passed",
            "No injection detected",
            "Performance stable"
        ],
        "recommendations": [
            "Continue monitoring",
            "Improve logging",
            "Regular audits required"
        ]
    })


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)