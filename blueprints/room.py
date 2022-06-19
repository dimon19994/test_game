from flask import Blueprint, request
from flask_login import login_required

from controllers.room import CreateRoomController, RoomListController


room = Blueprint("room", __name__)


@room.route('/rooms', methods=["POST"])
@login_required
def registration():
    return RoomListController(request).call()


@room.route("/create_room", methods=["POST"])
@login_required
def login():
    return CreateRoomController(request).call()
