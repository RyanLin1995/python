def tag(name, *content, class_=None, **attrs) -> str:  # 定义函数时，如果想指定仅限关键字参数，就把它们放到前面有*的参数后面
    """
        生成一个或多个HTML标签
    @param name: html 标签名称
    @param content: html 标签内容
    @param class_: html 标签属性
    @param attrs: 其他 html 属性
    @return: 一个 html标签字符串
    """
    if class_ is not None:
        attrs["class"] = class_
    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'


print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))  # 'hello', 'world' 都会被 *content 接收组成元祖
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', class_='sidebar'))  # class_ 只能作为关键词参数传入
print(tag(content='testing', name='img'))  # 即使传入 content 都是会被 attr 接收
my_tag = {'name': 'img', 'title': 'Test', 'src': 'test.jpg', 'class': 'frames'}
print(tag(**my_tag))  # 在 my_tag 前加上 ** 对 my_tag 进行解包后传递，字典中的项作为参数依次传入。同名键绑定到对应命名参数上，剩下的被 *attrs 捕捉
