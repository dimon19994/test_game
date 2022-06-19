CREATE TABLE users
(
    id       SERIAL NOT NULL PRIMARY KEY,
    username TEXT   NOT NULL UNIQUE,
    password TEXT   NOT NULL
);

CREATE TABLE tokens
(
    token   TEXT    NOT NULL PRIMARY KEY,
    user_id INTEGER NOT NULL,

    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE rooms
(
    id            SERIAL  NOT NULL PRIMARY KEY,
    name          TEXT    NOT NULL,
    max_players   INTEGER NOT NULL,
    players_count INTEGER NOT NULL DEFAULT 1,
    creator_id    INTEGER NOT NULL,

    FOREIGN KEY (creator_id) REFERENCES users (id)
);

CREATE TABLE users_in_room
(
    user_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,

    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (room_id) REFERENCES rooms (id)
);
