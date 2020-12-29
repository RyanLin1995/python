def set_func_1(func):
    def call_func():
        return "<h1>" + func() + "</h1>"

    return call_func


def set_func_2(func):
    def call_func():
        return "<title>" + func() + "</title>"

    return call_func


@set_func_1
@set_func_2
def test():
    return "hahahahah"


print(test())  # 最终结果应该是 <h1><title>hahahahah</title></h1>
