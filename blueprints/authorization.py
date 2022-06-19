from flask import Blueprint, request

from controllers.authorization import RegistrationController, LoginController


authorization = Blueprint("authorization", __name__)


@authorization.route('/registration', methods=["POST"])
def registration():
    return RegistrationController(request).call()


@authorization.route("/login", methods=["POST"])
def login():
    return LoginController(request).call()
