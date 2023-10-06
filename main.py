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

Write a SQL query to answer this question: {question}

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
