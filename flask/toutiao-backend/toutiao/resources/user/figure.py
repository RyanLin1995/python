from flask import g
from flask_restful import Resource

from cache import statistic as cache_statistic
from utils.decorators import login_required


class FigureResource(Resource):
    """
    用户统计数据
    """
    method_decorators = [login_required]

    def get(self):
        """
        获取用户统计数据
        """
        return {
            'fans_count': cache_statistic.UserFollowersCountStorage.get(g.user_id),
            'read_count': cache_statistic.UserArticlesReadingCountStorage.get(g.user_id)
        }
