from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test")
def test():
    return {"data": "success"}


if __name__ == "__main__":
    app.debug = True
    app.run()