from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

# 链接是需要指定要用到的MySQL数据库
engine = create_engine('mysql+pymysql://root:1158@localhost:3306/flask_1?charset=utf8')
Base = declarative_base()  # 生成SQLORM基类


class User(Base):
    # 对应MySQL中数据表的名字
    __tablename__ = 'user'

    # 创建字段
    id = Column(Integer, primary_key=True)
    user_id = Column(String(50), nullable=False)
    user_name = Column(String(50), nullable=False)
    head_img = Column(String(200))
    short_description = Column(String(300))