a = '菠菜,韭菜,花菜,西兰花,白菜,包菜,芹菜,青菜,辣椒,西芹,木耳,韭黄,蒜苔,油菜,生菜,蒜苗,水芹,茼蒿,芥菜,油菜,豆苗,小青菜,紫甘蓝,小白菜,娃娃菜,空心菜,地瓜叶,龙须菜,青豆,毛豆,扁豆,豌豆,蚕豆,四季豆,绿豆芽,豆苗,黄豆芽,香菇,草菇,平菇,金针菇,杏鲍菇,小平菇,冬瓜,南瓜,黄瓜,丝瓜,苦瓜,佛手瓜,大葱,蒜,姜,小葱,洋葱,山药,芋头,魔芋,红薯,紫薯,土豆,山药,莲藕,胡萝卜,白萝卜'
b = 'bocai,jiucai,huacai,xilanhua,baicai,baocai,qincai,qingcai,lajiao,xiqin,muer,jiuhuang,suantai,youcai,shengcai,suanmiao,shuiqin,tonghao,jiecai,youcai,doumiao,xiaoqingcai,ziganlan,xiaobaicai,wawacai,kongxincai,diguaye,longxucai,qingdou,maodou,biandou,wandou,candou,sijidou,lüdouya,doumiao,huangdouya,xianggu,caogu,pinggu,jinzhengu,xingbaogu,xiaopinggu,donggua,nangua,huanggua,sigua,kugua,foshougua,dacong,suan,jiang,xiaocong,yangcong,shanyao,yutou,moyu,hongshu,zishu,tudou,shanyao,lianou,huluobo,bailuobo'

a_list = a.split(',')
b_list = b.split(',')

for i in range(len(a_list)):
    print(a_list[i] + "\n" + b_list[i].upper() + "\n" + b_list[i].lower())
