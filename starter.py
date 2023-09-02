from flask import Flask, jsonify
from time import time

theMessage = "Automate all the things!" # Should I make this an env variable?

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def returnTime():
    unixTime = int(time())
    return jsonify(
        {
            'message': theMessage,
            'timestamp': unixTime
        }
    )