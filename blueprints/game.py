from flask_socketio import emit, send, join_room, leave_room, rooms
from flask import request, current_app

from app import socket_io


@socket_io.on('connect')
def test_connect(auth):
    emit('my response', {'data': 'Connected'})


@socket_io.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socket_io.on('join')
def on_join(data):
    username = data['username']
    room_name = data['room']
    join_room(room_name)
    send(username + f' has entered the room. {rooms(request.sid)} -> {socket_io.rooms[""]["room_name"]}', to=room_name)


@socket_io.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)