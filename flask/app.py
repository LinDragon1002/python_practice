from flask import Flask, request, render_template, redirect, url_for
import pymysql
from database import DB_CONFIG

app = Flask(__name__)

def get_db():
    """連接資料庫"""
    return pymysql.connect(**DB_CONFIG, cursorclass=pymysql.cursors.DictCursor)

# 前台 - 公告列表展示頁
@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    sql = "SELECT * FROM announcements ORDER BY create_time DESC"
    cursor.execute(sql)
    announcements = cursor.fetchall()
    conn.close()

    # 格式化時間
    for item in announcements:
        item['end_time'] = item['end_time'].strftime('%Y-%m-%d %H:%M')

    return render_template('list.html', datas=announcements)


# 管理後台 - 公告列表
@app.route('/admin')
def admin_list():
    conn = get_db()
    cursor = conn.cursor()
    sql = "SELECT * FROM announcements ORDER BY create_time DESC"
    cursor.execute(sql)
    announcements = cursor.fetchall()
    conn.close()

    # 格式化時間
    for item in announcements:
        item['end_time'] = item['end_time'].strftime('%Y-%m-%d %H:%M')

    return render_template('admin.html', datas=announcements)


# 新增公告頁面
@app.route('/admin/create', methods=['GET', 'POST'])
def create_page():
    if request.method == 'POST':
        # 處理表單提交
        title = request.form.get('title')
        content = request.form.get('content')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')

        conn = get_db()
        cursor = conn.cursor()
        sql = "INSERT INTO announcements (title, content, start_time, end_time) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql,(title, content, start_time, end_time))
        conn.commit()
        conn.close()

        return redirect(url_for('admin_list'))

    return render_template('create.html')


# 編輯公告頁面
@app.route('/admin/update/<int:id>', methods=['GET', 'POST'])
def update_page(id):
    conn = get_db()

    if request.method == 'POST':
        # 處理表單提交
        title = request.form.get('title')
        content = request.form.get('content')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')

        cursor = conn.cursor()
        sql = "UPDATE announcements SET title=%s, content=%s, start_time=%s, end_time=%s WHERE id=%s"
        cursor.execute(sql,(title, content, start_time, end_time, id))
        conn.commit()
        conn.close()

        return redirect(url_for('admin_list'))

    # GET - 顯示編輯表單
    cursor = conn.cursor()
    sql = "SELECT * FROM announcements WHERE id = %s"
    cursor.execute(sql, (id,))
    announcement = cursor.fetchone()
    conn.close()

    if not announcement:
        return "公告不存在", 404

    # 格式化日期為 YYYY-MM-DD 供表單使用
    announcement['start_time'] = announcement['start_time'].strftime('%Y-%m-%d')
    announcement['end_time'] = announcement['end_time'].strftime('%Y-%m-%d')

    return render_template('update.html', announcement=announcement)


# 刪除公告
@app.route('/admin/delete/<int:id>')
def delete_announcement(id):
    conn = get_db()
    cursor = conn.cursor()
    sql = "DELETE FROM announcements WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    conn.close()

    return redirect(url_for('admin_list'))

if __name__ == '__main__':
    # init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
