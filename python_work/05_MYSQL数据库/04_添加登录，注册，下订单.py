import pymysql


class GetData(object):

    def __init__(self):
        self.login_user_name = None
        self.connect = pymysql.connect(host="localhost", user="root", password="a12345",database="jingdong", charset="utf8")
        self.cursor = self.connect.cursor()
        self.login_or_not = False

    def __del__(self):

        self.cursor.close()
        self.connect.cursor()
        self.login_or_not = False

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
        item_name = input("输入要查询的名称:")
        sql_command = "select * from goods where name=%s;"
        self.cursor.execute(sql_command, [item_name])
        print(self.cursor.fetchall())

    def sign_in(self):
        self.login_user_name = input("用户名:")
        password = input("密码:")
        sql_command = "select * from customers where name=%s and password=%s;"
        self.cursor.execute(sql_command, [self.login_user_name, password])
        result = self.cursor.fetchall()
        if result:
            for name in result:
                if name[1] == self.login_user_name and name[-1] == password:
                    print("登陆成功!\n")
                    self.login_or_not = True
                    return

        else:
            sign_up_info = input("用户名不存在，请问是否注册账号(y/n):")
            if sign_up_info == "y":
                self.sign_up()
            elif sign_up_info == "n":
                print("请先注册账号/n")
            else:
                print("输入错误，请先注册账号!\n")

    def sign_up(self):
        user_name = input("请输入用户名:")
        addr = input("请输入收货地址:")
        tel = input("请输入电话号码:")
        password = input("密码:")
        sql_check_name_command = "select name from customers where name=%s;"
        self.cursor.execute(sql_check_name_command, [user_name])
        for name in self.cursor.fetchall():
            if name[0] == user_name:
                print("用户名已存在，请再输入用户名!\n")
            else:
                sql_command = "insert into customers values(0, %s, %s, %s, %s)"
                self.cursor.execute(sql_command, [user_name, addr, tel, password])
                self.connect.commit()
                if not self.cursor.fetchall():
                    print("注册成功!\n")

    def buy(self):
        if self.login_or_not:
            item = int(input("请输入要购买的产品的号码:"))
            if item:
                customer_id = "select id from customers where name=%s;"
                self.cursor.execute(customer_id, [self.login_user_name])
                id = self.cursor.fetchone()
                orders = "insert into orders values(0,0,%s)"
                self.cursor.execute(orders, id[0])

                quantity = int(input("请输入购买的数量:"))
                orders_id = "select id from orders;"
                self.cursor.execute(orders_id)
                orders_id = self.cursor.fetchall()[-1]
                order_detail = "insert into order_detail values(0,%s,%s,%s);"
                self.cursor.execute(order_detail, [orders_id, item, quantity])

                self.connect.commit()
                print("下单成功!\n")

        else:
            print("请先登录!\n")

    @staticmethod
    def print_menu():

        print("请选择你要查询的信息")
        print("---------------------------")
        print("1. 查询所有商品信息")
        print("2. 查询所有商品分类")
        print("3. 查询所有商品品牌分类")
        print("4. 添加一个商品分类")
        print("5. 输入要查询商品的名字")
        print("6. 登录")
        print("7. 注册")
        print("8. 下订单")
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

            if choose == "6":
                self.sign_in()

            if choose == "7":
                self.sign_up()

            if choose == "8":
                self.buy()

            if choose == "q" or choose == "0":
                exit()


def main():
    jd = GetData()
    jd.run()


if __name__ == '__main__':
    main()

