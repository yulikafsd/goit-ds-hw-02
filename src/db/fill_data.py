from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_USERS = 5
NUMBER_TASKS = 20
STATUSES = [("new",), ("in progress",), ("completed",)]


def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users = []
    fake_tasks = []

    """Create fake_data variable"""
    fake_data = faker.Faker()

    """Generate fake users"""
    for _ in range(number_users):
        fake_users.append([fake_data.name(), fake_data.ascii_email()])

    """Generate fake tasks"""
    for _ in range(number_tasks):
        fake_tasks.append([fake_data.catch_phrase(), fake_data.text(max_nb_chars=150)])

    return fake_users, fake_tasks


def prepare_data(fake_users, fake_tasks) -> tuple():
    """Prepare statuses for seeding"""
    for_statuses = []

    for status in STATUSES:
        for_statuses.append(status)

    """Prepare users for seeding"""
    for_users = []

    for user in fake_users:
        name, email = user
        for_users.append(
            (
                name,
                email,
            )
        )

    """Prepare tasks for seeding"""
    for_tasks = []

    for task in fake_tasks:
        title, descr = task
        for_tasks.append(
            (title, descr, randint(1, len(STATUSES)), randint(1, NUMBER_USERS))
        )

    return for_statuses, for_users, for_tasks


def insert_data_to_db(statuses, users, tasks) -> None:
    """Connect to DB and get cursor"""
    with sqlite3.connect("tasks.db") as con:
        cur = con.cursor()

        """Fill the statuses"""
        sql_to_statuses = """INSERT INTO status(name)
                            VALUES (?)"""
        cur.executemany(sql_to_statuses, statuses)

        """Fill the users"""
        sql_to_users = """INSERT INTO users(fullname, email)
                            VALUES (?, ?)"""
        cur.executemany(sql_to_users, users)

        """Fill the tasks"""
        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                            VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_tasks, tasks)

        """Commit the cnahges"""
        con.commit()


if __name__ == "__main__":

    fake_users, fake_tasks = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    statuses, users, tasks = prepare_data(fake_users, fake_tasks)
    insert_data_to_db(statuses, users, tasks)
