from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from sqlalchemy import extract

app = Flask(__name__)

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# MySQL 資料庫設定
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 類型 (types) 表
class items_types(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String(100), nullable=False)
    # 建立關聯，讓 `Item` 可以透過 `category` 取得 `type_name`
    items_name = db.relationship("money", backref="category")

# 收入/支出 (enorin) 表
class enorin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

# 消費項目 (transactions) 表
class money(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    enorin_id = db.Column(db.Integer, db.ForeignKey('enorin.id'), nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    type_id = db.Column(db.Integer, db.ForeignKey('items_types.id'), nullable=False)

# API: 新增類型
@app.route('/add_type', methods=['POST'])
def add_type():
    data = request.json
    new_type = items_types(items=data['items'])
    db.session.add(new_type)
    db.session.commit()
    return jsonify({"message": "類型已新增", "type_id": new_type.id})

# API: 取得所有類型
@app.route('/get_types', methods=['GET'])
def get_types():
    types = items_types.query.all()
    return jsonify([{"id": t.id, "items": t.items} for t in types])

# API: 新增消費項目
@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.json
    new_expense = money(
        name=data['name'],
        amount=data['amount'],
        enorin_id=data['enorin_id'],
        type_id=data['type_id'],
        date=data['date']
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"message": "消費項目已新增", "expense_id": new_expense.id})

# API: 尋找年月份
@app.route('/find_month/<year>/<month>', methods=['GET'])
def find_month(year,month):
    money_list = money.query.filter(
        extract('year', money.date) == year,  # 篩選年份
        extract('month', money.date) == month  # 篩選月份
    ).all()

    if money_list:
        return jsonify([
            {
                "name": i.name,
                "amount": i.amount,
                "date": i.date.strftime("%Y-%m-%d"),
                "type_name": i.category.items
            } for i in money_list
        ])

    # 沒有資料則回傳錯誤訊息
    return jsonify({"error": "No words found for this month"}), 404

# API: 尋找今日金額
@app.route('/today/<date>', methods=['GET'])
def today(today):
    money_list = money.query.filter_by(date=today).all()

    if money_list:
        return jsonify([
            {
                "name": i.name,
                "amount": i.amount,
                "date": i.date.strftime("%Y-%m-%d"),
                "type_name": i.category.items
            } for i in money_list
        ])

    # 沒有資料則回傳錯誤訊息
    return jsonify({"error": "No words found for this month"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)