from database import create_connection

def add_task(task):
    # Connect to the database
    conn = create_connection()
    cursor = conn.cursor()
    # Insert a new task into the 'tasks' table
    cursor.execute('''
        INSERT INTO tasks (title, description, due_date, priority, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (task.title, task.description, task.due_date, task.priority, task.status))
    conn.commit()  # Save the changes
    conn.close()   # Close the connection

def get_tasks():
    # Connect to the database
    conn = create_connection()
    cursor = conn.cursor()
    # Retrieve all tasks from the 'tasks' table
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()  # Fetch all results
    conn.close()   # Close the connection
    return tasks

def delete_task(task_id):
    # Connect to the database
    conn = create_connection()
    cursor = conn.cursor()
    # Delete a task from the 'tasks' table by task ID
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()  # Save the changes
    conn.close()   # Close the connection
