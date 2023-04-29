from flask_goods import goods_bp


@goods_bp.route('/goods')
def get_goods():
    return 'goods'
