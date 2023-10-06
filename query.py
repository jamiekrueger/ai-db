import argparse
from db import create_connection


def select_all_from_games(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM games")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_from_table(conn, query):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_example(conn, table):
    # Fetch column names
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    columns = [column[1] for column in cur.fetchall()]

    columns_formatted = ', '.join(columns)

    # Fetch rows
    query = f"SELECT * FROM {table} LIMIT 3"
    cur.execute(query)
    rows = cur.fetchall()
    rows_formatted = '\n'.join([', '.join(map(str, r)) for r in rows])

    return f"""
/*    
3 Example Rows:
SELECT * FROM {table} LIMIT 3;
{columns_formatted}
{rows_formatted}
*/
"""


if __name__ == "__main__":
    database = "./pythonsqlite.db"
    conn = create_connection(database)

    # select_all_from_games(conn)

    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, help="SELECT * FROM menu where unit_price >=55.0")
    args = parser.parse_args()
    print(f"Executing query: {args.query}")
    select_from_table(conn, args.query)
