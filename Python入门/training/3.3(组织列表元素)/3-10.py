#coding:gbk
game=["LOL" , "FIFA" , "WAR3" , "GTA5"]
print(game)
print("\n")
#打印list长度
print(len(game))
print("\n")
#对list进行临时排序（正序）
print(sorted(game))
print("\n")
#对list进行排序（反序）
print(sorted(game,reverse=True))
print("\n")
#对list进行永久性排序（正序）
game.sort()
print(game)
print("\n")
#对list进行永久性排序（反序）
game.sort(reverse=True)
print(game)
print("\n")
#反向打印list
game.reverse()
print(game)


