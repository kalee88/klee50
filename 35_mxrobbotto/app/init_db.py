import sqlite3

def create_tables():
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    # Create user table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        image_file TEXT NOT NULL DEFAULT 'default.jpg',
        password TEXT NOT NULL
    )
    ''')

    # Create story table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS story (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        date_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES user (id)
    )
    ''')

    # Create contribution table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contribution (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        story_id INTEGER NOT NULL,
        date_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES user (id),
        FOREIGN KEY (story_id) REFERENCES story (id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database initialized successfully.")
