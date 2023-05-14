from flask import g
from flask_restful import Resource

from cache import user as cache_user
from utils.decorators import login_required


class HistoryListResource(Resource):
    """
    搜索历史
    """
    method_decorators = [login_required]

    def get(self):
        """
        获取用户搜索历史
        """
        ret = cache_user.UserSearchingHistoryStorage(g.user_id).get()
        return {'keywords': ret}

    def delete(self):
        """
        删除搜索历史
        """
        cache_user.UserSearchingHistoryStorage(g.user_id).clear()
        return {'message': 'OK'}, 204
