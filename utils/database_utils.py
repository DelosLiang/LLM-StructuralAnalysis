import sqlite3
import os

def fetch_merged_text(db_path, main_number, sub_number):
    """
    Query merged_text for a specific request from SQLite database.

    Parameters:
        db_path (str): Database file path.
        main_number (int): Main number, e.g., 5.
        sub_number (int): Sub number, e.g., 1.

    Returns:
        str: Retrieved merged_text. Returns None if not found.
    """
    # Initialize user_message variable
    user_message = None

    # Check if database file exists
    if os.path.exists(db_path):
        try:
            # Connect to SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Construct sub_number
            target_path = f"{main_number}_{sub_number}"  # e.g., 5_1

            # Query path
            query = "SELECT merged_text FROM Requests WHERE sub_number = ?"

            # Execute query
            cursor.execute(query, (target_path,))
            result = cursor.fetchone()

            if result:
                # Extract query result content
                user_message = result[0].strip()
            else:
                print(f"Path not found: {target_path}")

        except sqlite3.Error as e:
            print("Database read failed:", e)

        finally:
            # Close database connection
            if conn:
                conn.close()

    else:
        print(f"Database file does not exist: {db_path}")

    return user_message

def fetch_ICL(db_path, main_number):
    """
    Query ICL_text for a specific number from SQLite database.

    Parameters:
        db_path (str): Database file path.
        main_number (int): Main number, e.g., 5.

    Returns:
        str: Retrieved ICL_text. Returns None if not found.
    """
    # Initialize ICL_text variable
    ICL_text = None

    # Check if database file exists
    if os.path.exists(db_path):
        try:
            # Connect to SQLite database
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Query ICL_text for specified main number
            query = "SELECT ICL_text FROM Texts WHERE number = ?"
            cursor.execute(query, (main_number,))
            result = cursor.fetchone()

            if result:
                # Extract query result content
                ICL_text = result[0].strip()
            else:
                print(f"Number not found: {main_number}")

        except sqlite3.Error as e:
            print("Database read failed:", e)

        finally:
            # Close database connection
            if conn:
                conn.close()

    else:
        print(f"Database file does not exist: {db_path}")

    return ICL_text
