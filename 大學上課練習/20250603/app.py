from flask import Flask, Response, json
import psycopg2

app = Flask(__name__)

# 資料庫連線字串
DB_URL = "postgresql://root:a38V7h0SlO19tNcU2xuH4ry6zIG5WoKs@hnd1.clusters.zeabur.com:32326/postgres"

def get_db_connection():
    return psycopg2.connect(DB_URL)

@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        # 建立連線
        conn = get_db_connection()
        cursor = conn.cursor()
        
        sql = '''
            select a.cusno,b.cusname,a.transfee from ordmaster a,customer b
            where a.cusno = b.cusno
        '''
        # 執行查詢
        cursor.execute(sql)
        
        # 取得所有結果
        rows = cursor.fetchall()
        
        # 包裝結果       
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        
        # 回傳JSON格式的結果，設定 ensure_ascii=False 讓中文正常顯示
        response = Response(
            response=json.dumps(result, ensure_ascii=False),
            content_type='application/json; charset=utf-8'
        )
        return response

    except Exception as e:
        error_response = Response(
            response=json.dumps({'error': str(e)}, ensure_ascii=False),
            content_type='application/json; charset=utf-8'
        )
        return error_response, 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
