from flask import Blueprint, current_app

bp = Blueprint('test', __name__)


@bp.route('/test')
def test():
    return f"ok {current_app.redis_cli}"
