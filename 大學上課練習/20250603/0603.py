import psycopg2

# 資料庫連線資訊
DB_URL = "postgresql://root:a38V7h0SlO19tNcU2xuH4ry6zIG5WoKs@hnd1.clusters.zeabur.com:32326/postgres"

try:
    # 建立連線
    conn = psycopg2.connect(DB_URL)
    cursor = conn.cursor()

    # 執行查詢
    sql = '''
        select * from customer
        where cusno not in (select distinct(cusno) from ordmaster)
        
        
    '''
    cursor.execute(sql)

    # 取得所有結果
    rows = cursor.fetchall()

    # 輸出查詢結果
    for row in rows:
        print(row)

except Exception as e:
    print("連線或查詢時發生錯誤：", e)

finally:
    # 關閉連線
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()