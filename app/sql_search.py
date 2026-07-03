import sqlite3


DATABASE_PATH = "database/hr.db"

def execute_query(query):
    """Execute a SQL query against the HR database and return its rows.

    Args:
        query: The SQL statement to execute.

    Returns:
        A list of database rows returned by the query.
    """

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute(query)

    columns = [
        column[0]
        for column in cursor.description
    ]

    rows = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows

def get_table_schema(table_name: str) -> str:
    """
    Return the SQLite schema for the given table.

    Args:
        table_name:
            Name of the database table.

    Returns:
        A formatted schema string.

    Example:

        employees(
            id INTEGER,
            name TEXT,
            department TEXT,
            salary INTEGER,
            leave_balance INTEGER
        )

    Raises:
        RuntimeError:
            If the schema cannot be read.
    """

    try:

        conn = sqlite3.connect(DATABASE_PATH)

        cursor = conn.cursor()

        cursor.execute(f"PRAGMA table_info({table_name})")

        columns = cursor.fetchall()

        conn.close()

        if not columns:
            raise RuntimeError(f"Table '{table_name}' does not exist.")

        schema = []

        for column in columns:

            column_name = column[1]

            column_type = column[2]

            schema.append(
                f"    {column_name} {column_type}"
            )

        return (
            f"{table_name}(\n"
            + ",\n".join(schema)
            + "\n)"
        )

    except sqlite3.Error as e:

        raise RuntimeError(
            f"Failed to read schema for table '{table_name}'."
        ) from e
    
def get_database_schema() -> str:
    """Return the schema for every table in the database.

    Returns:
        A string containing the schema for each table separated by blank lines.
    """

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    )

    tables = cursor.fetchall()

    conn.close()

    schemas = []

    for table in tables:

        schemas.append(
            get_table_schema(table[0])
        )

    return "\n\n".join(schemas)

