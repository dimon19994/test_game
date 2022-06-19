# @socketio.on('connect')
# def test_connect(auth):
#     if auth is None:
#         pass
#     emit('my response', {'data': 'Connected'})
#
# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')
#
# @socketio.on('join')
# def on_join(data):
#     username = data['username']
#     room = data['room']
#     join_room(room)
#     send(username + f' has entered the room. {request.sid}', to=room)
#
# @socketio.on('leave')
# def on_leave(data):
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(username + ' has left the room.', to=room)