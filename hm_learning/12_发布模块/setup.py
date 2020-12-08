from distutils.core import setup

setup(name='hm_message',  # 包名
      version='1.0',  # 版本
      description='发送和接收消息模块',  # 描述信息
      long_description='完成的发送和接收消息模块',  # 完整描述信息
      author='Ryan',  # 作者
      author_email='a563645043@gmail.com',  # 作者邮件
      py_modules=['hm_message.send_message',
                  'hm_message.receive_message'])
