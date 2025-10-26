import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def fetch_text_by_number(number):
    # Get database path from environment variable
    db_path = os.getenv("ICL_DB_PATH", "data/ICL.db")
    
    # 连接 SQLite 数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 根据编号查询数据
    cursor.execute("SELECT * FROM Texts WHERE number = ?", (number,))
    result = cursor.fetchone()
    conn.close()

    # 如果找到数据，则返回；否则提示未找到
    if result:
        return f"ID: {result[0]}, Number: {result[1]}, Description: {result[2]}, Related Text: {result[3]}"
    else:
        return "No data found with that number."

if __name__ == "__main__":
    print("Retrieve stored text by number:")
    while True:
        try:
            number = int(input("Enter the number (or type 0 to exit): "))
            if number == 0:
                print("Exiting the program. Goodbye!")
                break

            result = fetch_text_by_number(number)
            print(result)
        except ValueError:
            print("Please enter a valid number.")
