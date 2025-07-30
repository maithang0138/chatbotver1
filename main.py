from flask import Flask, request, render_template, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Cài đặt API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Bạn là trợ lý AI thân thiện."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content'].strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
