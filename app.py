# Author: Omer Mirza
# Date: 08/31/2023
# Description: Simple Flask app that returns current time

from flask import Flask, jsonify
from time import time
import os

# Passes MESSAGE environment variable to the request.
# Allows for easier modification without App redeployment.

app = Flask(__name__)

# Returns UNIX time when called by GET or POST request.
@app.route('/', methods = ['GET', 'POST'])
def returnTime():
    unixTime = int(time())
    theMessage = os.environ['MESSAGE']
    return jsonify(
        {
            'message': theMessage,
            'timestamp': unixTime
        }
    )
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
