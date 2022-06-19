from app import app
from .authorization import authorization
from .room import room


app.register_blueprint(authorization)
app.register_blueprint(room)
