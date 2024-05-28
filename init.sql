CREATE TABLE IF NOT EXISTS users(
    chat_id BIGINT PRIMARY KEY,
    username TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS pari(
    id BIGSERIAL PRIMARY KEY,
    pari_name TEXT NOT NULL,
    challenger_name TEXT,
    taker_name TEXT
)