import sqlite3

connect = sqlite3.connect('orders.db')
current = connect.cursor()

current.executescript('''PRAGMA foreign_keys=on;
                        CREATE TABLE IF NOT EXISTS books(
                                                        Id INTEGER PRIMARY KEY,
                                                        title TEXT NOT NULL,
                                                        count_page INTEGER NOT NULL CHECK (count_page >0),
                                                        price REAL CHECK (price >0),
                                                        auth_id INTEGER NOT NULL,
                                                        FOREIGN KEY (auth_id) REFERENCES auth(id));

                        CREATE TABLE IF NOT EXISTS auth(
                                                       id INTEGER PRIMARY KEY,
                                                       name TEXT NOT NULL,
                                                       age INTEGER CHECK (age >16));''')

current.executescript("""INSERT INTO auth (id, name, age) VALUES (1, 'Джек Лондон', 40);
                         INSERT INTO auth (id, name, age) VALUES (2, 'Лев Толстой', 82);""")

current.executescript("""INSERT INTO books (id, title, count_page, price, auth_id)
                                          VALUES (1, ‘Белый’, 287, 300.00, 1);
                         INSERT INTO books (id, title, count_page, price, auth_id)
                                          VALUES (2, ‘Война и мир’, 806, 780.00, 2);""")


connect.commit()
