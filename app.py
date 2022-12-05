import subprocess
import socket
from flask import Flask, request
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics, PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/')
def hello():
    ip = socket.gethostbyname(socket.gethostname())
    cmd = "curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone"
    zone = subprocess.check_output(cmd, shell=True)
    return f'[{zone}] "hello! {app}" from {ip}'


if __name__ == "__main__":
    
    app.run("0.0.0.0", 5000)
    
