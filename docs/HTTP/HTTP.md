## HTTP
2019/4/26  [返回](https://desperadoadil.github.io/FlaskLearning/)

---
- HTTP方法没什么好说的  

- HTTP请求  
    - 请求处理  
        ```python
        @app.route('/hello', methods = ['GET', 'POST'])
        @app.route('/goback/<int:year>')
        @app.route('/colors/<any>(red, blue, white):color')
        @app.route('/<path:path>')
        ```
        转换器类型：string(默认),int,float,path,any,uuid  
    - 请求钩子  
        - before_first_request()  
        - before_request()  
        - after_request()  
        - teardown_request()  
        - after_this_request()  
- HTTP响应  
    - 2xx 成功  
        200 OK  
        201 Created  
        202 Accepted  
        204 No Content  
    - 3xx 重定向  
        301 Moved Permanently  
        302 Found  
        304 Not Modified  
    - 4xx 客户端错误  
        400 Bad Request  
        401 Unauthorized  
        403 Forbidden  
        404 Not Found  
        405 Method Not Allowed  
        409 Conflict  
        410 Gone  
        429 Too Many Requests  
    - 5xx 服务端错误  
        500 Internal Server Error  
        503 Service Unavailable  
    - abort()函数抛出错误响应  
    - 响应格式 `response.headers['Content-Type']`  
        - `text/plain`  
        - `text/html`  
        - `application/xml`  
        - `application/json`  
    - Cookie, Session  
- Flask 上下文  
    - 程序上下文  
        - current_app  
        - g  
    - 请求上下文  
        - request  
        - session  
- Web 安全  
    这个之后会仔细研究  
