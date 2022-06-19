from peewee import JOIN
from uuid import uuid4
from flask_login import login_user, current_user

from controllers import _Controller
from models.tables import Room, UsersInRoom


class CreateRoomController(_Controller):
    def _post(self):
        creator = self.request.json["creatorId"]
        room_name = self.request.json["roomTitle"]
        max_players = self.request.json["playersCount"]

        room = Room.create(name=room_name, max_players=max_players, creator=creator)
        UsersInRoom.create(room_id=room, user_id=current_user)

        return {"status": 'Ok'}



class RoomListController(_Controller):
    def _post(self):
        user_name = self.request.json.get("userName")
        password = self.request.json.get("password")
        token = self.request.json.get("token")

        if token is not None:
            user = User.select().join(Token, JOIN.LEFT_OUTER).where(Token.token == token).first()

            if user is not None:
                login_user(user)
                return {"status": 'Ok', "userId": user.id}
            else:
                return {"status": 'Failed'}

        else:
            user = User.select().join(Token, JOIN.LEFT_OUTER)\
                .where((User.username == user_name) & (User.password == password)).first()

            if user is not None:
                token = str(uuid4())
                Token.create(user_id=user.id, token=token)

                return {"status": 'Ok', "userId": user.id, "AUTH_TOKEN": token}
            else:
                return {"status": 'Failed'}
