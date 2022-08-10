# sqlite3 with python

Exercise using Python with the [sqlite3](https://docs.python.org/3/library/sqlite3.html) DB-API interface for [SQLite](https://www.sqlite.org/index.html) databases.

It starts by creating a `Connection` to a local `database.db` file that allow to create an sample table of `users` and perform SQL commands to consult, add, update and delete users through a `Cursor` object.

Run any of the following commands in the project's root to run the exercise.

```
python main.py
```

```
python3 main.py
```

The file `database.db` is purged every run.

Versions used in development:

- `SQLite 3.31.1`.
- `Python 3.8.10`
