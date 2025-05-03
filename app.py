import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return "AI Chatbot Backend is running."

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": user_input}]
        }
    )

    if response.status_code == 200:
        output = response.json()['choices'][0]['message']['content']
        return jsonify({"response": output})
    else:
        return jsonify({"response": "Error from OpenAI backend."}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
