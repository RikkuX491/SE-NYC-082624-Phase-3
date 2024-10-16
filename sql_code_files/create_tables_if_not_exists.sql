CREATE TABLE IF NOT EXISTS hotels (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY,
    rating INTEGER,
    text TEXT,
    hotel_id INTEGER,
    customer_id INTEGER
);