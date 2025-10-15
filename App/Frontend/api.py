from flask import Flask, jsonify, request
from chat import Chat

chatFlow = Chat()
app = Flask(__name__)

@app.route('/input', methods=['POST'])
def add_message():
    new_message = request.get_json()
    output = chatFlow.post_message(new_message)

    return output

app.run(port=3000, host='localhost', debug=True)
