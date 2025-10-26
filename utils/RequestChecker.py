import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def fetch_request_by_sub_number(sub_number):
    # Get database path from environment variable
    db_path = os.getenv("REQUEST_DB_PATH", "data/request.db")
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query for the specific sub-request
    cursor.execute("SELECT * FROM Requests WHERE sub_number = ?", (sub_number,))
    result = cursor.fetchone()
    conn.close()

    # If data is found, format the result; otherwise, indicate no data found
    if result:
        return f"ID: {result[0]}\nSub-Number: {result[1]}\nDescription: {result[2]}\nMerged Text:\n{result[3]}"
    else:
        return "No data found with that sub-number."

if __name__ == "__main__":
    print("Retrieve stored requests by sub-number:")
    while True:
        try:
            number = int(input("Enter the main request number (or type 0 to exit): "))
            if number == 0:
                print("Exiting the program. Goodbye!")
                break

            sub_number = input(f"Enter the sub-number for request {number} (e.g., {number}_1): ")
            result = fetch_request_by_sub_number(sub_number)
            print(result)
        except ValueError:
            print("Please enter a valid number.")
