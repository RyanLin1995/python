import pymysql


class GetData(object):

    def __init__(self):
        self.connect = pymysql.connect(host ="localhost", user="root", password="a12345",
                                  database="jingdong", charset="utf8")
        self.cursor = self.connect.cursor()

    def __del__(self):

        self.cursor.close()
        self.connect.cursor()

    def execute_sql(self, sql_command):

        self.cursor.execute(sql_command)
        for item in self.cursor.fetchall():
            print(item)

    def show_all_items(self):

        sql_command = "select * from goods;"
        self.execute_sql(sql_command)

    def show_cates(self):

        sql_command = "select name from goods_cates;"
        self.execute_sql(sql_command)

    def show_brands(self):

        sql_command = "select name from goods_brands;"
        self.execute_sql(sql_command)

    def add_cates(self):
        item_name = str(input("输入新商品分类的名称:"))
        sql_command = "insert into goods_cates (name) values ('{}');".format(item_name)
        self.cursor.execute(sql_command)
        # self.connect.rollback()
        self.connect.commit()

    def get_info_from_name(self):
        """该设置中，如果在 input 中输入 ' or 1=1 or '1 ，那么会把所有的信息全部呈现
        原理是因为 sql 语句中直接使用了单引号，该问题也叫 sql注入 """
        item_name = input("输入要查询的名称:")
        # sql_command = "select * from goods where name='{}';".format(item_name)

        # 因此，推荐将需要查询的数值放在一个列表中，把 sql 语句中的符号去掉
        sql_command = "select * from goods where name=%s;"  # pymysql 的原因，只能用 %s，不能用{}
        self.cursor.execute(sql_command, [item_name])  # pymysql 语句支持直接传入列表，元祖，字典
        print(self.cursor.fetchall())


    @staticmethod
    def print_menu():

        print("请选择你要查询的信息")
        print("---------------------------")
        print("1. 查询所有商品信息")
        print("2. 查询所有商品分类")
        print("3. 查询所有商品品牌分类")
        print("4. 添加一个商品分类")
        print("5. 输入要查询商品的名字")
        return input("请输入:")

    def run(self):

        while True:
            choose = self.print_menu()
            if choose == "1":
                self.show_all_items()

            if choose == "2":
                self.show_cates()

            if choose == "3":
                self.show_brands()

            if choose == "4":
                self.add_cates()

            if choose == "5":
                self.get_info_from_name()

            if choose == "q" or choose == "0":
                exit()


def main():
    jd = GetData()
    jd.run()


if __name__ == '__main__':
    main()

