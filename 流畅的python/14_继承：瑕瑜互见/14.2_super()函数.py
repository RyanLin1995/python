# 1. 继承时尽可能使用 super() 而不是基类名
# 2. super() 在 Python3 接收两个可选参数 type 跟 object_or_type。
# type：从哪里开始搜索实现所需方法的超类；
# object_or_type：接收方法调用的对象（调用实例方法时）或类（调用类方法时）、在实例方法中调用 super() 时，默认为 self
