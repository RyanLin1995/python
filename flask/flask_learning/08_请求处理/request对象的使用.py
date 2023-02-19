from flask import Flask, request

app = Flask(__name__)


# 如果想要获取其他地方传递的参数，可以通过Flask提供的request对象来读取。
# 不同位置的参数都存放在request的不同属性中
# 属性	     说明	                        类型
# data	     记录请求的数据，并转换为字符串	    *
# form	     记录请求中的表单数据	            MultiDict
# args	     记录请求中的查询参数	            MultiDict
# cookies	 记录请求中的cookie信息	        Dict
# headers	 记录请求中的报文头	            EnvironHeaders
# method	 记录请求使用的HTTP方法	        GET/POST
# url	     记录请求的URL地址	            string
# files	     记录请求上传的文件	            *

@app.route('/articles')
def get_users_id():
    channel_id = request.args.get('channel_id')
    return str(channel_id)


@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['pic']
    # with open('./demo.png', 'wb') as new_file:
    #     new_file.write(f.read())
    f.save('./demo.png')
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
