import sqlite3
import os

def fetch_merged_text(db_path, main_number, sub_number):
    """
    从 SQLite 数据库中查询特定 request 的 merged_text。

    参数：
        db_path (str): 数据库文件路径。
        main_number (int): 主编号，例如 5。
        sub_number (int): 副编号，例如 1。

    返回：
        str: 查询到的 merged_text。如果未找到则返回 None。
    """
    # 初始化 user_message 变量
    user_message = None

    # 检查数据库文件是否存在
    if os.path.exists(db_path):
        try:
            # 连接到 SQLite 数据库
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # 构造 sub_number
            target_path = f"{main_number}_{sub_number}"  # e.g., 5_1

            # 查询路径
            query = "SELECT merged_text FROM Requests WHERE sub_number = ?"

            # 执行查询
            cursor.execute(query, (target_path,))
            result = cursor.fetchone()

            if result:
                # 提取查询结果内容
                user_message = result[0].strip()
            else:
                print(f"未找到路径：{target_path}")

        except sqlite3.Error as e:
            print("数据库读取失败：", e)

        finally:
            # 关闭数据库连接
            if conn:
                conn.close()

    else:
        print(f"数据库文件不存在：{db_path}")

    return user_message

def fetch_ICL(db_path, main_number):
    """
    从 SQLite 数据库中查询特定 number 的 ICL_text。

    参数：
        db_path (str): 数据库文件路径。
        main_number (int): 主编号，例如 5。

    返回：
        str: 查询到的 ICL_text。如果未找到则返回 None。
    """
    # 初始化 ICL_text 变量
    ICL_text = None

    # 检查数据库文件是否存在
    if os.path.exists(db_path):
        try:
            # 连接到 SQLite 数据库
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # 查询指定主编号的 ICL_text
            query = "SELECT ICL_text FROM Texts WHERE number = ?"
            cursor.execute(query, (main_number,))
            result = cursor.fetchone()

            if result:
                # 提取查询结果内容
                ICL_text = result[0].strip()
            else:
                print(f"未找到编号：{main_number}")

        except sqlite3.Error as e:
            print("数据库读取失败：", e)

        finally:
            # 关闭数据库连接
            if conn:
                conn.close()

    else:
        print(f"数据库文件不存在：{db_path}")

    return ICL_text
