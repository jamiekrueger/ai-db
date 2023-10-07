import argparse
import openai
import os

from query import select_from_table
from schema import get_schema, get_schema_with_examples
from db import create_connection
from dotenv import load_dotenv

DATABASE = "./pythonsqlite.db"


def get_prompt_string(question, strategy):
    if strategy == 1:
        return f"""

Given the following SQL Schema:{get_schema()}

Write a SQL query to answer this question: {question}
 
"""
    elif strategy == 2:
        return f"""

Given the following SQL Schema:{get_schema_with_examples()}

Write a valid SQLite query to answer this question: {question}

"""
    elif strategy == 3:
        return f"""

Given the following SQL Schema:{get_schema_with_examples()}

Write a valid SQLite query to answer the following questions for the tables provided above: 

Question: Which game is most popular with people over the age of 50?

SELECT g.name, COUNT(*) as num_players_over_50
FROM games as g
INNER JOIN orders as o on g.gameId = o.gameId
INNER JOIN customers as c on o.customerId = c.customerId
WHERE timediff(date(),
                substr(c.birthdate, -4) ||
                '-' ||
                printf('%02d', CAST(substr(c.birthdate, 1, instr(c.birthdate, '/') - 1) AS INT)) ||
                '-' ||
                printf('%02d', CAST(substr(c.birthdate, instr(c.birthdate, '/') + 1, length(c.birthdate) - instr(c.birthdate, '/') - 5) AS INT))
            ) > timediff(date(),strftime('%Y-%m-%d', 'now', '-50 years'))
GROUP BY g.name
ORDER BY num_players_over_50 DESC
LIMIT 1;

Question: What game is closest to selling out?

SELECT g.name AS game_name, i.quantity
FROM inventory i
JOIN games g ON i.gameId = g.gameId
ORDER BY i.quantity ASC
LIMIT 1;

Question: Show the names of each customer that has purchased multiple games.

SELECT c.name
FROM customers c
JOIN orders o ON c.customerId = o.customerId
GROUP BY c.customerId, c.name
HAVING COUNT(o.gameId) > 1;

Question: What is the average score for games made by skynoodle?

SELECT AVG(rating) AS average_score
FROM games AS g
JOIN reviews AS r ON g.gameId = r.gameId
WHERE g.publisher = 'Skynoodle';

Question: {question}
"""


def main(conn, question, strategy):
    load_dotenv()

    openai.api_key = os.getenv("OPENAI_API_KEY")
    print(f"Question: {question}")

    prompt = get_prompt_string(question, strategy)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=200
    )

    q = response["choices"][0]["text"]

    print(f"AI-generated SQL query: \n{q}")
    print("Answer: \n")
    select_from_table(conn, q)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, default="natural language query")
    parser.add_argument("--strategy", type=int, default=1)
    args = parser.parse_args()
    conn = create_connection(DATABASE)

    main(conn, question=args.query, strategy=args.strategy)


