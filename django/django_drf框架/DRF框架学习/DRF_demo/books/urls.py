from rest_framework.routers import SimpleRouter

from books import modelviewset_view

urlpatterns = [
    # path('books/', genericapiview_view.BooksView.as_view()),
    # re_path(r'books/(?P<pk>\d+)', genericapiview_view.BookView.as_view())

    # Viewset 路由使用
    # path('books/', viewset_view.BooksView.as_view({'get': 'list', 'post': 'create'})),
    # # Viewset 路由匹配需要传入字典参数，key 为请求方式，value 为 view 中方法名
    # re_path(r'^books/(?P<pk>\d+)$', viewset_view.BookView.as_view({'put': 'update'})),
    # # 如果 Viewset 中的方法超过以下5个方法的话，路由的匹配如下:
    # # list() 提供一组数据
    # # retrieve() 提供单个数据
    # # create() 创建数据
    # # update() 保存数据
    # # destory() 删除数据
    # re_path(r'^books/(?P<pk>\d+)/lastdata$', viewset_view.BookView.as_view({'get': 'lastdata'})),  # url 后边要带有该方法名

    # GenericaViewSet 路由使用，与 viewset 使用方法一致
    # path('books/', genericaviewset_view.BooksView.as_view({'get': 'list', 'post': 'create'})),
    # re_path(r'^books/(?P<pk>\d+)$', genericaviewset_view.BookView.as_view({'put': 'update'})),
    # re_path(r'^books/(?P<pk>\d+)/lastdata$', genericaviewset_view.BookView.as_view({'get': 'lastdata'})),

    # ModelViewSet 路由使用，与 viewset 使用方法一致，但是因为 ModelViewSet 继承了视图集父类，所以带有 list() 等函数，不需要定义也可以使用
    # path('books/', modelviewset_view.BooksView.as_view({'get': 'list', 'post': 'create'})),
    # re_path(r'^books/(?P<pk>\d+)$',
    #         modelviewset_view.BooksView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),
]

# 自动生成路由（只适用于结合视图集使用，且自定义方法需要在方法中使用 action 装饰器生成url）
# 1. 先定义一个 SimpleRouter 的实例对象
router = SimpleRouter()
# router = DefaultRouter()  # DefaultRouter 继承于 SimpleRouter，只不过 DefaultRouter 有对首页的路由而 SimpleRouter 没有
# 2. 调用 router 的 register 方法
router.register('books', modelviewset_view.BooksView, basename='books')  # 第一个参数为 url , 第二个参数为 view， 第三个参数为 反向代理名称
# 3. 添加路由到 urlpatterns
urlpatterns += router.urls
