import os

if os.path.exists("database.db"):
    os.remove("database.db")

from sqlite3 import Error, connect


def connect_with_db():
    try:
        connection = connect("database.db")
        print("Successfully connected to the database")
        return connection
    except Error:
        print("An error has occurred")


def create_users_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            first_name TEXT NOT NULL, 
            last_name TEXT NOT NULL
        )
        """
    )
    connection.commit()


def insert_single_user(connection, data):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)", data)
    connection.commit()


def insert_multiple_users(connection, data):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO users (first_name, last_name) VALUES (?, ?)", data)
    connection.commit()


def consult_all_users(connection):
    print("Consulting all")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    found_users = cursor.fetchall()
    if len(found_users) == 0:
        print("Users not found")
    for user in found_users:
        print(user)


def consult_user_by_id(connection, id):
    print(f"Consulting user with id={id}")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (id,))
    found_users = cursor.fetchall()
    if len(found_users) == 0:
        print("Users not found")
    for user in found_users:
        print(user)


def update_user_by_id(connection, id, data):
    print(f"Updating user with id={id}")
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE users SET first_name = ?, last_name = ? WHERE id = ?", (*data, id)
    )
    connection.commit()


def delete_user_by_id(connection, id):
    print(f"Deleting user with id={id}")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    connection.commit()


connection = connect_with_db()

print("\nCREATE TABLE")
create_users_table(connection)
consult_all_users(connection)

print("\nADD A SINGLE USER")
single_user = ("John", "Doe")
insert_single_user(connection, single_user)
consult_all_users(connection)

print("\nADD MULTIPLE USERS")
multiple_users = [("Mary", "Hilton"), ("James", "Smith")]
insert_multiple_users(connection, multiple_users)
consult_all_users(connection)

print("\nCONSULT BY ID")
consult_user_by_id(connection, 3)
consult_user_by_id(connection, 4)

print("\nUPDATE USER BY ID")
update_user_by_id(connection, 2, ("Rose", "Adams"))
consult_all_users(connection)

print("\nDELETE USER BY ID")
delete_user_by_id(connection, 1)
consult_all_users(connection)

connection.close()
