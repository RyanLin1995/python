class Game(object):

    # 历史最高分
    top_score = 0

    @staticmethod
    def show_help():
        print('帮助信息: 让僵尸进入大门')

    @classmethod
    def show_yop_score(cls):
        print('历史记录{}'.format(cls.top_score))

    def __init__(self, player_name):

        self.player_name = player_name

    def start_game(self):

        print('{} 开始游戏了'.format(self.player_name))


# 1. 查看游戏的帮助信息
Game.show_help()

# 2.查看历史做高分
Game.show_yop_score()

# 3. 创建游戏对象
game = Game('小明')
game.start_game()