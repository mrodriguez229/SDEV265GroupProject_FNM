import sqlite3

# Function to create a connection to the SQLite database
def create_connection():
    conn = None
    try:
        # Connect to the 'tasks.db' SQLite database
        conn = sqlite3.connect('tasks.db')
    except sqlite3.Error as e:
        # Print any connection error
        print(e)
    return conn

# Function to create the 'tasks' table if it doesn't exist
def create_tables():
    # Establish a database connection
    conn = create_connection()
    cursor = conn.cursor()
    # Create the 'tasks' table with columns for id, title, description, due date, priority, and status
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority TEXT,
            status TEXT
        )
    ''')
    conn.commit()  # Save the changes to the database
    conn.close()   # Close the connection

# Create the tables when this script is executed
create_tables()
