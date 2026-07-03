from pathlib import Path

try:
    import sqlite3
except ImportError as e:
    raise RuntimeError(
        "sqlite3 is required for database operations. "
        "Please install Python with SQLite support."
    ) from e


def create_database() -> None:
    """
    Create the HR database and employees table.
    """

    try:

        Path("database").mkdir(exist_ok=True)

        conn = sqlite3.connect("database/hr.db")

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (

                id INTEGER PRIMARY KEY,
                name TEXT,
                department TEXT,
                salary INTEGER,
                leave_balance INTEGER

            )
            """
        )

        conn.commit()
        conn.close()

        print("Database created successfully.")

    except sqlite3.Error as e:

        raise RuntimeError(
            f"Failed to create database 'database/hr.db': {e}"
        ) from e


if __name__ == "__main__":
    create_database()