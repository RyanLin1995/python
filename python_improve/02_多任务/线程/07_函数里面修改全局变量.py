num = 100
num_list = [100, 200]


def test1():
    global num

    num += 1


def test2():

    num_list.append(300)


print(num)
print(num_list)

test1()
test2()

print(num)
print(num_list)


