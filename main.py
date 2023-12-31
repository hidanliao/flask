import pymysql
from flask import Flask, render_template
from sqlalchemy.orm import sessionmaker

from models.models import engine, User

app = Flask(__name__, static_folder='assets')

@app.route("/profile2")
def index():
    return "First Web"

# @app.route("/<int:user_id>")
# def profile5(user_id):
#     with open("profile.html", encoding="utf-8") as f:
#         content = f.read()
#
#     content = content.replace("xxxxxxx", str(user_id))
#
#     return content

# @app.route("/<int:user_id>")
# def profile6(user_id):
#
#     return render_template("profile.html", user_name="Liao", user_head_img="329291347.png")

# @app.route("/<int:user_id>")
# def profile6(user_id):
#     # 1.业务处理
#     # ================= 这里添加新代码 ====================
#     # 1. 查询数据库
#     # 1.1 创建Connection连接
#     conn = pymysql.connect(host='localhost', port=3306, database='flask_1', user='root', password='1158',
#                            charset='utf8')
#     # 1.2 获得Cursor对象
#     cs1 = conn.cursor()
#     # 1.3 构造参数列表
#     params = [user_id]
#     # 1.4 执行select语句，并返回受影响的行数：查询所有数据
#     cs1.execute('select * from user where user_id=%s', params)
#     # 1.5 获取查询的结果
#     result = cs1.fetchone()
#     # result = cs1.fetchall()
#     print(result)
#     # 1.6 关闭Cursor对象
#     cs1.close()
#     # 1.7 闭Connection对象
#     conn.close()
#     # 2.模板替换
#     # return render_template("profile.html", user_name="Liao", user_head_img="329291347.png")
#     return render_template("profile.html", user_name=result[2], user_head_img=result[3], short_desc=result[4])

# @app.route("/<int:user_id>")
# def profile6(user_id):
#     # 1.业务处理
#     # 创建session对象
#     session = sessionmaker(bind=engine)()  # 生成链接数据库的实例
#
#     # 获取返回数据的第一行
#     user_ret = session.query(User).filter(User.user_id == user_id).one()
#     print(user_ret)
#
#     # 关闭session
#     session.close()
#
#     # 2.模板替换
#     # return render_template("profile.html", user_name="Liao", user_head_img="329291347.png")
#     return render_template("profile.html", user_name=user_ret.user_name, user_head_img=user_ret.head_img, short_desc=user_ret.short_description)

@app.route("/<int:user_id>")
def profile6(user_id):
    # 1.业务处理
    # 创建session对象
    session = sessionmaker(bind=engine)()  # 生成链接数据库的实例

    # 获取返回数据的第一行
    user_ret = session.query(User).filter(User.user_id == user_id).one()
    print(user_ret)

    # 关闭session
    session.close()

    # 2.模板替换
    # return render_template("profile.html", user_name="Liao", user_head_img="329291347.png")
    # return render_template("profile.html", user_name=user_ret.user_name, user_head_img=user_ret.head_img, short_desc=user_ret.short_description)
    return render_template("profile2.html", user=user_ret)

app.run(debug=True,)
# app.run()
# print(app.url_map)