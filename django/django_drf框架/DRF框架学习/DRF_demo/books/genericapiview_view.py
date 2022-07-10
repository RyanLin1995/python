import json

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from books.models import BookInfo
from books.serializers import BookSerializer


# Create your views here.


class BooksView(GenericAPIView):
    """
        获取所有和保存
    """
    queryset = BookInfo.objects.all().filter(isdelete=False)  # GenericAPIView 需要先指定当前类视图使用的查询集
    serializer_class = BookSerializer  # GenericAPIView 需要先指定当前类视图使用的序列化器

    def get(self, request):
        # 1. 查询所有图书对象
        books = self.get_queryset()  # 获取查询集中的所有数据

        # 2. 返回图书数据
        ser = self.get_serializer(books, many=True)  # 使用指定序列化器获取序列化对象
        return Response(ser.data)

    def post(self, request):
        # 1. 获取前端数据
        data_dict = request.data
        # 2. 验证数据
        # 序列化器验证数据
        ser = self.get_serializer(data=data_dict)  # 使用指定序列化器获取序列化对象
        ser.is_valid(raise_exception=True)
        print(ser.validated_data)

        # 3. 保存数据
        # 序列化器保存
        ser.save()

        # 4. 返回结果
        # 序列化器返回
        return Response(ser.errors)  # 继承 ref apiview 之后，response 方法也需要改变，统一为 Response


class BookView(GenericAPIView):
    """
        获取单一数据、更新和删除
    """
    queryset = BookInfo.objects.all()  # GenericAPIView 需要先指定当前类视图使用的查询集
    serializer_class = BookSerializer  # GenericAPIView 需要先指定当前类视图使用的序列化器

    def get(self, request, pk):  # 获取单一数据
        print(request.query_params)
        # 1. 查询数据对象
        try:
            book = self.get_object()  # 从查询集中获取指定的单一数据对象，即会自动从查询集查询到匹配 pk 值的数据
        except:
            return Response({'error': '错误信息'}, status=400)

        # 使用序列化器
        ser = self.get_serializer(data=book)
        return Response(ser.data)

    def put(self, request, pk):  # 更新
        # 1. 获取前端数据
        data_dict = request.data
        print(data_dict)

        # 序列化器更新操作
        # 2. 验证数据
        try:
            book = self.get_object()
        except:
            return Response({'error': '错误信息'}, status=400)

        ser = self.get_serializer(book, data=data_dict)
        ser.is_valid()
        print(ser.validated_data)

        # 3. 更新数据
        ser.save()

        # 4. 返回数据
        return Response(ser.data)

    def delete(self, request, pk):  # 删除
        # 1. 查询数据对象
        try:
            book = self.get_object()
        except:
            return Response({'error': '错误信息'}, status=400)

        book.isdelete = True
        book.save()
        return Response({})
