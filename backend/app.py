from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)
api = Api(app)

openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/chat', methods=['POST'])
def chat():
  data = request.get_json()
  message = data.get('message', '')

  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=message,
    max_tokens=150
  )

  reply = response.choices[0].text.strip()
  return jsonify({'reply': reply})

if __name__ == '__main__':
  app.run(debug=True)
