import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Ollama Chatbot is running."

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": user_input,
            "stream": False
        }
    )

    if response.status_code == 200:
        output = response.json()['response']
        return jsonify({"response": output})
    else:
        return jsonify({"response": "Error from Ollama backend."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
