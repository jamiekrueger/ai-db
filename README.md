# cs452-ai-db

## SQL Lite DB with Python Client

To build, run the build script build the database and create the tables:
```
python3 build.py
```
This command creates the file `pythonssqlite.db`

Finally, to execute query run this command:
```
python3 main.py --query "{your query goes here}" --strategy {int}
```
For example, try running this query:
```
python3 query.py --query "SELECT * FROM menu where unit_price >=55.0" --strategy 1
```
You should see this result printed to your terminal:
```
Executing query: SELECT * FROM menu where unit_price >=55.0
(4, 'Espresso', 2, 55.0)
(5, 'Cappucino', 2, 55.0)
(6, 'Latte', 2, 55.0)
(7, 'Mocha', 2, 55.0)
(8, 'Passion Fruit', 3, 60.0)
(9, 'Mango Juice', 3, 60.0)
(10, 'Orange Juice', 3, 60.0)
```

*Note: for the full table schema definitions, see `schema.py`*
