CREATE TABLE IF NOT EXISTS menu(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pets(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
petname TEXT NOT NULL,
description TEXT NOT NULL,
time INTEGER NOT NULL
);
