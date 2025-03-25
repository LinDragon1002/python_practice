from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

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

if __name__ == '__main__':
    app.run(port=5000, debug=True)