from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_login import LoginManager


app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.init_app(app)

app.config.from_object('config')
app.config["SECRET_KEY"] = "test_key"
socket_io = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)
CORS(app)

import blueprints
