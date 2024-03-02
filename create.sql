-- Creating database
USE hbnb_dev_db;

CREATE TABLE IF NOT EXISTS states (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id VARCHAR(60) NOT NULL PRIMARY KEY,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    name VARCHAR(128) NOT NULL,
    state_id VARCHAR(60) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);
