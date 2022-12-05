import subprocess
import socket
from flask import Flask, Blueprint
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

CONFIG = {"version": "v0.1.2", "config": "staging"}
MAIN = Blueprint("main", __name__)
app = Flask(__name__)


def register_blueprints(app):
    """
    Register blueprints to the app
    """
    app.register_blueprint(MAIN)

@app.route('/')
def hello():
    ip = socket.gethostbyname(socket.gethostname())
    cmd = "curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone"
    zone = subprocess.check_output(cmd, shell=True)
    return f'[{zone}] "hello! {app}" from {ip}'

def create_app(config):
    """
    Application factory
    """
    app = Flask(__name__)

    register_blueprints(app)
    register_metrics(app, app_version=config["version"], app_config=config["config"])
    return app


def create_dispatcher() -> DispatcherMiddleware:
    """
    App factory for dispatcher middleware managing multiple WSGI apps
    """
    main_app = create_app(config=CONFIG)
    return DispatcherMiddleware(main_app.wsgi_app, {"/metrics": make_wsgi_app()})


if __name__ == "__main__":
    run_simple(
        "0.0.0.0",
        5000,
        create_dispatcher(),
        use_reloader=True,
        use_debugger=True,
        use_evalex=True,
    )
#     app.run()
    
