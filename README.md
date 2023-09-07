# Overview
- - - 
This is an application written in the Python programming language exposes a REST endpoint that returns the following JSON payload with the *current timestamp* and a *static message*:

```json
{
	"message": "Automate all the things!",
	"timestamp" : 1529729125
}
```

# Code
- - - 

```python
from flask import Flask, jsonify
from time import time
import os
```

Flask includes several built in functions that make creating HTTP REST applications simpler.

```python
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
```

The application processes get and post requests and returns:
- A message corresponding to a set environment variable
- The Unix Timestamp from the request

Flask also renders a front end interface when accessed from a web browser. Frontend code can be placed on top of this application for further application development.

# Docker File
- - - 

Below is a snippit of the dockerfile in this repo:

```Dockerfile
ENV MESSAGE="Automate all the things!"
ENV PORT="80"
EXPOSE 80 3000
```

The important thing to note with this file is that two environment variables are set by default. 
- When deploying arguments can be set to change these environment variables when the container is being created. 
- In effect, the message displayed to the end user and the exposed port can be modified by creating a new container instead of modifying the python code or the dockerfile.
# Questions
- - - 
## What is Flask?
- It has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.

## Why Flask over other libraries like Fast API?
- Flask performs well at sending REST API responses, but it is also designed to be extendable. 

- If this project were to be extended in the future, you wouldn't have to redo anything from scratch. 

## Does Flask conform to REST standards?
- **Yes**, if you don't use external libraries or if you use the `flask-restful` library