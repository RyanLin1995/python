# property 属性: 一种用起来像是使用实例属性一样的特殊属性
# 例子

class Foo(object):

    @property  # 在方法前加上@property，使方法成为@property方法
    def test(self):  # property 方法只传递一个形参self
        return 100  # property 方法始终返回一个值


obj = Foo()
print(obj.test)  # 调用 property 方法时，不需要添加()

print("--------------------------")


# 一个案例
# 对于京东商城中显示电脑主机的列表页面，每次请求不可能把数据库中的所有内容都显示到页面上，而是通过分页的功能局部显示，所以在向数据库中请求数据时就要显示的指定获取从第m条到第n条的所有数据这个分页的功能包括：
# 根据用户请求的当前页和总数据条数计算出 m 和 n
# 根据m 和  去数据库中请求数据

# ############### 定义 ###############
class Pager:
    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


# ############### 调用 ###############
p = Pager(1)
print(p.start)  # 就是起始值，即：m
print(p.end)  # 就是结束值，即：n
