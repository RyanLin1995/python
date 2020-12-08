class Gun:

    def __init__(self, model):

        # 1. 枪的型号
        self.model = model
        # 2. 子弹的数量
        self.bullet = 0

    def add_bullet(self, count):

        self.bullet += count

    def shoot(self):

        # 1. 判断子弹数量
        if self.bullet <= 0:
            print("[{}] ,没有子弹了...".format(self.model))
            return

        # 2. 发射子弹, -1
        self.bullet -= 1

        # 3. 提示发射信息
        print("[{}] biubiubiu... [{:g}]".format(self.model, self.bullet))


# 1. 创建枪对象
ak47 = Gun("AK47")
ak47.add_bullet(30)
ak47.shoot()
