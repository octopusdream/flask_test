import subprocess
import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    ip = socket.gethostbyname(socket.gethostname())
    cmd = "curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone"
    zone = subprocess.check_output(cmd, shell=True)
    return f'[{zone}] "hello!" from {ip}'

if __name__ == '__main__':
    app.run()
