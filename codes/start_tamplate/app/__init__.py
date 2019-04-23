from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)                               #注册Flask实例app
app.config.from_object('config')                    #加载配置
db = SQLAlchemy(app, use_native_unicode="utf8")     #注册数据库ORM实例db

from app import views, models                       #导入其他文件
