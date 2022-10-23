from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# 重写 jwt 返回方法
def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }


class PageNum(PageNumberPagination):
    """
        自定义的分页器
    """
    page_size_query_param = 'pagesize'
    max_page_size = 10

    # 由于当前分页器返回的结果不适用于前端，需要重写继承类的返回信息
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'lists': data,
            'page': self.page.number,
            'pages': self.page.paginator.num_pages,
            'pagesize': self.max_page_size
        })
