import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# 設定 MySQL 連接資訊
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE")
}

# 建立資料庫連線
def get_db_connection():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn

def execute_query(sql, params=None, fetchone=False):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, params or ())
    data = cursor.fetchone() if fetchone else cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data