import subprocess
import socket
from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

app = Flask(__name__)

@app.route('/')
def hello():
    ip = socket.gethostbyname(socket.gethostname())
    cmd = "curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone"
    zone = subprocess.check_output(cmd, shell=True)
    return f'[{zone}] "hello! {app}" from {ip}'



if __name__ == '__main__':
    # provide app's version and deploy environment/config name to set a gauge metric
    register_metrics(app, app_version="v0.1.2", app_config="staging")

    # Plug metrics WSGI app to your main app with dispatcher
    dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

    run_simple(hostname="localhost", port=5001, application=dispatcher)
    app.run()
