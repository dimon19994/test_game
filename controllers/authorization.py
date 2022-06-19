from peewee import JOIN
from uuid import uuid4
from flask_login import current_user, login_user

from controllers import _Controller
from models.tables import User, Token


class RegistrationController(_Controller):
    def _post(self):
        print(self.request.data)
        print(self.request.json if self.request.is_json else "XYZ")
        user_name = self.request.form["userName"]
        password = self.request.form["password"]
        password_confirm = self.request.form["passwordConfirm"]

        user = User.get_or_none(User.username == user_name)

        if user is not None:
            return {"status": 'Exist'}
        elif password != password_confirm:
            return {"status": 'Not match'}
        else:
            User.create(username=user_name, password=password)
            return {"status": 'Ok'}


class LoginController(_Controller):
    def _post(self):
        user_name = self.request.form.get("userName")
        password = self.request.form.get("password")
        token = self.request.form.get("token")

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
