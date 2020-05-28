# coding:utf-8
import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# 当前程序运行路径
base_dir = os.path.abspath(os.path.dirname(__file__))
# print('base_dir: \n', base_dir)

# connexion实例
connex_app = connexion.App(__name__, specification_dir=base_dir)

# flask实例
app = connex_app.app

# 配置app中SQLAlchemy的信息
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'people.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化SQLAlchemy
db = SQLAlchemy(app)

# 初始化Marshmallow
ma = Marshmallow(app)