from flask import Flask

app = Flask(__name__)

@app.route("/test")
def test():
    return {"data": "success"}


if __name__ == "__main__":
    app.debug = True
    app.run()