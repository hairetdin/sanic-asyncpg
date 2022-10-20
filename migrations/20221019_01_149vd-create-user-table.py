"""
create user table
"""

from yoyo import step

__depends__ = {}


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        # query to perform the migration
        "CREATE TABLE users (id INT, name VARCHAR(20), PRIMARY KEY (id))"
    )


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        # query to undo the above
        "DROP TABLE users"
    )


steps = [
    step(apply_step, rollback_step)
    # or
    # step("CREATE TABLE users (id INT, name VARCHAR(20), PRIMARY KEY (id))", "DROP TABLE users")
]
