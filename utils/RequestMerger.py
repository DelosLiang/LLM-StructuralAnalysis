import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_database():
    # Get database path from environment variable
    db_path = os.getenv("REQUEST_DB_PATH", "data/request.db")
    
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table if it doesn't already exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sub_number TEXT NOT NULL UNIQUE,
        description TEXT NOT NULL,
        merged_text TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def add_or_update_request(sub_number, description, merged_text):
    # Get database path from environment variable
    db_path = os.getenv("REQUEST_DB_PATH", "data/request.db")
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Check if sub_number already exists
    cursor.execute("""
    SELECT id FROM Requests WHERE sub_number = ?
    """, (sub_number,))
    result = cursor.fetchone()

    if result:
        # Update the existing entry
        cursor.execute("""
        UPDATE Requests
        SET description = ?, merged_text = ?
        WHERE sub_number = ?
        """, (description, merged_text, sub_number))
    else:
        # Insert a new entry
        cursor.execute("""
        INSERT INTO Requests (sub_number, description, merged_text)
        VALUES (?, ?, ?)
        """, (sub_number, description, merged_text))

    conn.commit()
    conn.close()

def merge_context_with_files(problem_context):
    # Get file paths from environment variables or use defaults
    data_dir = os.getenv("DATA_DIR", "data")
    param_file = os.path.join(data_dir, "param_config.txt")
    main_file = os.path.join(data_dir, "main.txt")
    post_proc_file = os.path.join(data_dir, "post_proc.txt")

    # Read the content of the files
    try:
        with open(param_file, 'r') as f:
            param_content = f.read()
        with open(main_file, 'r') as f:
            main_content = f.read()
        with open(post_proc_file, 'r') as f:
            post_proc_content = f.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None, None, None

    # Merge the problem context with the file contents
    merged_param = f"Problem Context:\n{problem_context}\n\nParam Config Content:\n{param_content}"
    merged_main = f"Problem Context:\n{problem_context}\n\nMain Content:\n{main_content}"
    merged_post_proc = f"Problem Context:\n{problem_context}\n\nPost-Processing Content:\n{post_proc_content}"

    return merged_param, merged_main, merged_post_proc

def main():
    create_database()

    print("Enter requests to store in the database. Enter '0' as the number to exit:")
    while True:
        try:
            number = int(input("Enter request number (or 0 to exit): "))
            if number == 0:
                print("Exiting the program. Goodbye!")
                break

            description = input("Enter description: ")
            problem_context = input("Enter problem context: ")

            merged_param, merged_main, merged_post_proc = merge_context_with_files(problem_context)

            if merged_param and merged_main and merged_post_proc:
                # Save to database with sub-numbers
                add_or_update_request(f"{number}_1", description, merged_param)
                add_or_update_request(f"{number}_2", description, merged_main)
                add_or_update_request(f"{number}_3", description, merged_post_proc)
                print(f"Request {number} and its sub-requests have been successfully added or updated in the database.")
            else:
                print("Failed to merge and save request.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
