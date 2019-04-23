## 一个最简单的Flask应用
2019/4/23  [返回](https://desperadoadil.github.io/FlaskLearning/)

---
[View on Github](https://github.com/DesperadoAdil/FlaskLearning/codes/start_template/)  
项目结构:
```python
|-- start_template
    |-- .gitignore              #gitignore
    |-- config.py               #项目配置文件
    |-- README.md               #README
    |-- requirements.txt        #依赖库文件
    |-- run.py                  #项目启动入口
    |-- app                     #项目实例app
        |-- models.py           #表结构文件
        |-- views.py            #视图函数文件
        |-- __init__.py         #__init__
        |-- static              #静态文件目录
        |-- templates           #模板文件目录
```

- /app/\_\_init\_\_.py
    ```python
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)                               #注册Flask实例app
    app.config.from_object('config')                    #加载配置
    db = SQLAlchemy(app, use_native_unicode="utf8")     #注册数据库ORM实例db

    from app import views, models                       #导入其他文件
    ```

- /run.py
    ```python
    from app import app

    app.run(debug = True, host = "0.0.0.0", port = 80)
    ```
    启动项目app，开启debug模式，主机端口为`localhost:80`  
    **需要注意的是：**  从Flask 1.0开始建议使用`$ flask run`来启动项目  
