import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    response = requests.post(
        "https://your-llm-api.com/api/generate",
        json={
            "model": "gemma:2b",  # 👈 use the correct model name
            "prompt": user_input,
            "stream": False
        }
    )

    if response.status_code == 200:
        output = response.json()['response']
        return jsonify({"response": output})
    else:
        return jsonify({"response": "Error from LLM backend."})

if __name__ == '__main__':
    app.run(debug=True)
