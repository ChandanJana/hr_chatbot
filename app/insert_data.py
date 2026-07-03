import sqlite3

conn = sqlite3.connect("database/hr.db")

cursor = conn.cursor()

cursor.execute("""

INSERT INTO employees

(name, department, salary, leave_balance)

VALUES

('John','IT',50000,20)

""")

cursor.execute("""

INSERT INTO employees

(name, department, salary, leave_balance)

VALUES

('Alice','HR',45000,15)

""")

conn.commit()

conn.close()