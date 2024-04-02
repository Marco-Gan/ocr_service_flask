from flask import Flask #导入Flask类

app = Flask(__name__) #创建一个Flask实例

@app.route('/')
def index():
   return '<h3>welcome to my webpage!</h3><hr><p style="color:red">56789</p>' #定义路由，当访问根目录时，返回welcome to my webpage!

if __name__ == '__main__':
    app.run(port=2020,host="127.0.0.1",debug=True)  #调用run方法，设定端口号，启动服务

