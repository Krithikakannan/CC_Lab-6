from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"Served by backend: {hostname}"

app.run(host="0.0.0.0", port=8080)
