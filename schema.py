from db import create_connection
from query import select_example

sql_create_customers_table = """
CREATE TABLE customers (
    customerId INT PRIMARY KEY,
    name TEXT,
    birthdate TEXT,
    gender TEXT
);
"""

sql_create_games_table = """
CREATE TABLE games (
    gameId INT PRIMARY KEY,
    name TEXT,
    category TEXT,
    description TEXT,
    publisher TEXT,
    playtime INT,
    numPlayers INT
);
"""

sql_create_inventory_table = """
CREATE TABLE inventory (
    gameId INT PRIMARY KEY,
    price TEXT,
    quantity INT,
    FOREIGN KEY (gameId) references games(gameId)
);
"""

sql_create_orders_table = """
CREATE TABLE orders (
    orderId INT PRIMARY KEY,
    customerId INT,
    gameId INT,
    FOREIGN KEY (customerId) references customers(customerId)
    FOREIGN KEY (gameId) references games(gameId)
);
"""

sql_create_reviews_table = """
CREATE TABLE reviews (
    reviewId INT PRIMARY KEY,
    customerId INT,
    gameId INT,
    comment TEXT,
    rating REAL,
    FOREIGN KEY (customerId) references customers(customerId)
    FOREIGN KEY (gameId) references games(gameId)
);
"""


def get_schema():
    schema = f"{sql_create_customers_table}{sql_create_games_table}{sql_create_inventory_table}{sql_create_orders_table}{sql_create_reviews_table}"
    return schema


def get_schema_with_examples():
    conn = create_connection("./pythonsqlite.db")
    schema = f"{sql_create_customers_table}{select_example(conn, 'customers')}{sql_create_games_table}{select_example(conn, 'games')}{sql_create_inventory_table}{select_example(conn, 'inventory')}{sql_create_orders_table}{select_example(conn, 'orders')}{sql_create_reviews_table}{select_example(conn, 'reviews')}"
    return schema

