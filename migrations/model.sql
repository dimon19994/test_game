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
