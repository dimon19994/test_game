from app import socket_io, app
from config import TestConfig


if __name__ == '__main__':
    socket_io.run(app, debug=True, host='0.0.0.0', port=25565, use_reloader=False)
