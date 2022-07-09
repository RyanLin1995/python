import json

from books.serializers import BookSerializer

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from books.models import BookInfo


# Create your views here.


class BooksView(View):
    """
        获取所有和保存
    """

    def get(self, request):
        # # 1. 查询所有图书对象
        books = BookInfo.objects.all()
        # print(books)
        # # 2. 返回图书数据
        # book_list = []
        # for book in books:
        #     book_list.append(
        #         {
        #             'id': book.id,
        #             'btitle': book.btitle,
        #             'bread': book.bread,
        #             'bcomment': book.bcomment,
        #             'bpub_date': book.bpub_date,
        #         }
        #     )
        # return JsonResponse(book_list, safe=False)

        # 使用序列化器
        ser = BookSerializer(books, many=True)  # 返回多个查询对象要加上 many=Truefro
        return JsonResponse(ser.data, safe=False)

    def post(self, request):
        # 1. 获取前端数据
        data = request.body.decode()  # 因为 json 通过请求体传递，所以要从 body 获取
        data_dict: dict = json.loads(data)
        # 2. 验证数据
        # btitle = data_dict.get('btitle')
        # bpub_date = data_dict.get('bpub_date')
        # if not all([btitle, bpub_date]):
        #     return JsonResponse({'error': '错误信息'}, status=400)

        # 序列化器验证数据
        ser = BookSerializer(data=data_dict)
        ser.is_valid(raise_exception=True)  # 验证方法，raise_exception=True 自动返回错误信息
        print(ser.validated_data)  # 显示验证后的数据

        # 3. 保存数据
        # book = BookInfo.objects.create_book(btitle=btitle, bpub_date=bpub_date)

        # 序列化器保存
        ser.save()  # save 会自动调用 serializers.py 中的 create 方法

        # 4. 返回结果
        # return JsonResponse({
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment,
        #     'bpub_date': book.bpub_date,
        # })

        # 序列化器返回
        return JsonResponse(ser.errors, safe=False)


class BookView(View):
    """
        获取单一数据、更新和删除
    """

    def get(self, request, pk):  # 获取单一数据
        # 1. 查询数据对象
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '错误信息'}, status=400)

        # return JsonResponse({
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment,
        #     'bpub_date': book.bpub_date,
        # })

        # 使用序列化器
        ser = BookSerializer(book)
        return JsonResponse(ser.data, safe=False)

    def put(self, request, pk):  # 更新
        # 1. 获取前端数据
        data = request.body.decode()  # 因为 json 通过请求体传递，所以要从 body 获取
        data_dict: dict = json.loads(data)
        print(data_dict)

        # 普通更新操作
        # # 2. 验证数据
        # btitle = data_dict.get('btitle')
        # bpub_date = data_dict.get('bpub_date')
        # if not all([btitle, bpub_date]):
        #     return JsonResponse({'error': '错误信息'}, status=400)
        # # 3. 更新数据
        # try:
        #     book = BookInfo.objects.get(id=pk)
        # except:
        #     return JsonResponse({'error': '错误信息'}, status=400)
        # book.btitle = btitle
        # book.bpub_date = bpub_date
        # book.save()
        # # 4. 返回结果
        # return JsonResponse({
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment,
        #     'bpub_date': book.bpub_date,
        # })

        # 序列化器更新操作
        # 2. 验证数据
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '错误信息'}, status=400)

        ser = BookSerializer(book, data=data_dict)  # 更新数据需要传递要更新的对象，这里要更新的对象就是 book
        ser.is_valid()
        print(ser.validated_data)

        # 3. 更新数据
        ser.save()  # 因为 ser 实例对象传递了 book 对象(即 isinstance 对象)，所以 save 方法调用的是 serializers.py 中的 update 方法

        # 4. 返回数据
        return JsonResponse(ser.data, safe=False)

    def delete(self, request, pk):  # 删除
        # 1. 查询数据对象
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '错误信息'}, status=400)

        book.isdelete = True
        book.save()
        return JsonResponse({})
