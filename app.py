import os
import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    ip = socket.gethostbyname(socket.gethostname())
    zone = os.environ.get('ZONE', '')
    return f'[{zone}] "hello!" from {ip}'

if __name__ == '__main__':
    app.run()
