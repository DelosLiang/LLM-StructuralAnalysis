import sqlite3

def create_database():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("ICL.db")
    cursor = conn.cursor()

    # Create the table if it doesn't already exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Texts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number INTEGER NOT NULL UNIQUE,
        description TEXT NOT NULL,
        ICL_text TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def add_or_update_text(number, description, ICL_text):
    # Connect to the SQLite database
    conn = sqlite3.connect("ICL.db")
    cursor = conn.cursor()

    # Check if the number already exists
    cursor.execute("SELECT id FROM Texts WHERE number = ?", (number,))
    row = cursor.fetchone()

    if row:
        # Update the existing entry
        cursor.execute("""
        UPDATE Texts
        SET description = ?, ICL_text = ?
        WHERE number = ?
        """, (description, ICL_text, number))
        print(f"Updated entry for number {number}.")
    else:
        # Insert a new entry
        cursor.execute("""
        INSERT INTO Texts (number, description, ICL_text)
        VALUES (?, ?, ?)
        """, (number, description, ICL_text))
        print(f"Added new entry for number {number}.")

    conn.commit()
    conn.close()

def view_numbers():
    # Connect to the SQLite database
    conn = sqlite3.connect("ICL.db")
    cursor = conn.cursor()

    # Retrieve all unique numbers from the table
    cursor.execute("SELECT DISTINCT number FROM Texts")
    rows = cursor.fetchall()
    conn.close()

    # Print only the unique numbers
    numbers = [row[0] for row in rows]
    print("Numbers stored in the database:", numbers)

if __name__ == "__main__":
    create_database()

    # Allow the user to input texts
    print("Enter texts to store in the database. Enter '0' as the number to exit:")
    count = 0  # Counter to track how many texts have been added
    while count < 20:
        try:
            number = int(input("Enter number (or 0 to exit): "))
            if number == 0:
                print("Exiting the program. Goodbye!")
                break
            description = input("Enter description: ")
            txt_file_path = input("Enter the path to the text file for ICL text: ")
            try:
                with open(txt_file_path, 'r') as file:
                    ICL_text = file.read()
            except FileNotFoundError:
                print("File not found. Please enter a valid file path.")
                continue
            add_or_update_text(number, description, ICL_text)
            print("Operation successful!\n")
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

    print("\nAll numbers stored in the database:")
    view_numbers()
