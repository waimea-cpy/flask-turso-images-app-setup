--===========================================================
-- DB Schema, used to initialise the database
--===========================================================


CREATE TABLE IF NOT EXISTS things (
    `id`    INTEGER PRIMARY KEY AUTOINCREMENT,
    `name`  TEXT NOT NULL,
    `price` INTEGER NOT NULL
);

