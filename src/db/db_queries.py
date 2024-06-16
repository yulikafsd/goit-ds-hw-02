import sqlite3
from typing import List, Tuple, Any

db_path = "tasks.db"  # Path to db


# SELECT-query function
def execute_query(sql: str, params: Tuple[Any, ...] = ()) -> List[Tuple[Any, ...]]:
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(sql, params)
        return cur.fetchall()


# Non-SELECT-query function (UPDATE, DELETE, INSERT)
def execute_non_select_query(sql: str, params: Tuple[Any, ...] = ()) -> None:
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        cur.execute(sql, params)
        con.commit()


# Отримати всі завдання певного користувача за його user_id
all_users_tasks_query = """
SELECT title 
FROM tasks 
WHERE user_id = ?;
"""
# print(execute_query(all_users_tasks_query, (1,)))

# Вибрати завдання за певним статусом, наприклад, 'new'
tasks_by_status_query = """
SELECT title
FROM tasks
WHERE status_id IN (SELECT id FROM status WHERE name = ?);
"""
# print(execute_query(tasks_by_status_query, ("new",)))

# Оновити статус конкретного завдання на 'in progress'
update_status_query = """
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = ?)
WHERE user_id = ?;
"""
# execute_non_select_query(update_status_query, ("in progress", 5))

# Отримати список користувачів, які не мають жодного завдання (всі завдання completed)
users_wo_tasks_query = """
SELECT *
FROM users
WHERE id NOT IN (SELECT user_id FROM tasks WHERE status_id = 1 OR status_id = 2);
"""
# print(execute_query(users_wo_tasks_query))

# Додати нове завдання для конкретного користувача
insert_new_task_query = """
INSERT INTO tasks (title, description, status_id, user_id)
VALUES (?, ?, ?, ?);
"""
title = "This is a brand new task"
description = "This is a description, that should be maximum 150 literals long"
status_id = 1
user_id = 3
# execute_non_select_query(
#     insert_new_task_query, (title, description, status_id, user_id)
# )

# Отримати всі завдання, які ще не завершено
users_with_uncompleted_tasks_query = """
SELECT *
FROM users
WHERE id IN (SELECT user_id FROM tasks WHERE status_id = 1 OR status_id = 2);
"""
# print(execute_query(users_with_uncompleted_tasks_query))

# Видалити конкретне завдання за його id
delete_task_query = """
DELETE FROM tasks WHERE id = ?;
"""
# execute_non_select_query(delete_task_query, (20,))

# Знайти користувачів з певною електронною поштою
users_by_email_query = """
SELECT *
FROM users
WHERE email LIKE ?;
"""
# print(execute_query(users_by_email_query, ("ebonyallen@gmail.com",)))

# Оновити ім'я користувача
update_user_name_query = """
UPDATE users
SET fullname = ?
WHERE id = ?;
"""
# execute_non_select_query(update_user_name_query, ("Name Updated", 3))

# Отримати кількість завдань для кожного статусу
count_tasks_by_status_query = """
SELECT COUNT(*), s.name
FROM tasks t
LEFT JOIN status s ON t.status_id = s.id
GROUP BY s.id;
"""
# print(execute_query(count_tasks_by_status_query))

# Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
tasks_by_userdomain_query = """
SELECT t.title
FROM tasks t
LEFT JOIN users u ON t.user_id = u.id
WHERE u.email LIKE ?;
"""
# print(execute_query(tasks_by_userdomain_query, ("%@gmail.com",)))

# Отримати список завдань, які не мають опису
tasks_wo_description_query = """
SELECT *
FROM tasks
WHERE description IS NULL;
"""
# print(execute_query(tasks_wo_description_query))

# Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
users_with_inprogress_tasks_query = """
SELECT t.title, u.fullname
FROM tasks t
INNER JOIN users u ON t.user_id = u.id
WHERE t.status_id = 2;
"""
# print(execute_query(users_with_inprogress_tasks_query))

# Отримати користувачів та кількість їхніх завдань
count_tasks_by_user_query = """
SELECT COUNT(*), u.fullname
FROM tasks t
LEFT JOIN users u ON t.user_id = u.id
GROUP BY u.fullname;
"""
# print(execute_query(count_tasks_by_user_query))
