FROM python:3.9-slim-buster

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

# Sets the default message variable
ENV MESSAGE="Automate all the things!"
ENV PORT="80"
# Port 80 is exposed in Azure by default for AKS traffic
# Port 3000 is exposed for local docker containers
# Port 5000 is used by ControlCenter on MacOS
EXPOSE 80 3000

# Executes the application
CMD python ./app.py