class Setting():

    def __init__(self):
        """这里存储了设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 800
        self.bg = (195, 195, 195)
        self.little_ship_speed = 2.3
        # 子弹设置
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_speed_factor = 1.8
        self.bullet_color = 102, 102, 102
        # 方块速度
        self.rect_speed = 1
        self.rect_direction = 1
