from app import app
from .authorization import authorization


app.register_blueprint(authorization)
