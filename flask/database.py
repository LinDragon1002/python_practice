from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('host'),
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'database': os.getenv('database')
}















# def init_db():
#     """初始化資料庫"""
#     conn = pymysql.connect(
#         host=DB_CONFIG['host'],
#         user=DB_CONFIG['user'],
#         password=DB_CONFIG['password']
#     )

#     with conn.cursor() as cursor:
#         cursor.execute("CREATE DATABASE IF NOT EXISTS practice_birc")
#         cursor.execute("USE practice_birc")
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS announcements (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 title VARCHAR(255) NOT NULL,
#                 content TEXT NOT NULL,
#                 start_time DATETIME NOT NULL,
#                 end_time DATETIME NOT NULL,
#                 create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#             )
#         """)
#     conn.commit()
#     conn.close()
#     print("資料庫初始化完成")