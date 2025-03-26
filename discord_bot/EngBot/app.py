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
class eng_dictionary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(45),nullable=False)
    definition = db.Column(db.String(200), nullable=False)
    example = db.Column(db.String(200), nullable=False)
    translation = db.Column(db.String(100),nullable=False)
    abbreviation = db.Column(db.String(100),nullable=False)

# API: 新增單字
@app.route('/add_voc', methods=['POST'])
def add_type():
    data = request.json
    new_voc = eng_dictionary(
        word=data['word'],
        abbreviation=data['abbreviation'],
        definition=data['definition'],
        example=data['example'],
        translation=data['translation']
    )
    db.session.add(new_voc)
    db.session.commit()
    return jsonify({"message": "單字已新增", "type_id": new_voc.id})

# API: 查單字
@app.route('/check_voc/<word>', methods=['GET'])
def checkvoc(word):
    checkvoc = eng_dictionary.query.filter_by(word=word).first()
    if checkvoc:
        return jsonify({
            "word":checkvoc.word,
            "translation":checkvoc.translation,
            "abbreviation":checkvoc.abbreviation,
            "definition":checkvoc.definition,
            "example":checkvoc.example
        })
    else:
        return jsonify({"error": "Word not found"}), 404

# API: 列出所有單字
@app.route('/allvoc', methods=['GET'])
def allvoc():
    checkvoc = eng_dictionary.query.with_entities(eng_dictionary.word).all()
    word_list = [word[0] for word in checkvoc]
    return jsonify(word_list)

# API: 刪除單字
@app.route('/del_voc/<word>', methods=['GET'])
def delvoc(word):
    checkvoc = eng_dictionary.query.filter_by(word=word).first()
    if checkvoc:
        db.session.delete(checkvoc)  # 刪除資料
        db.session.commit()  # 提交變更
        return jsonify({"message": f"'{word}' has been deleted."})
    
    return jsonify({"error": "Word not found"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)