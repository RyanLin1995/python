import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 在队列 _queue 上插入第一个元素，并且队列 _queue 保证第一个元素拥有最高优先级
        heapq.heappush(self._queue, (-priority, self._index, item))

        # index 变量的作用是保证同等优先级元素的正确排序。通过保存一个不断增加的 index 下标变量，可以确保元素按照它们插入的顺序排序。
        # 而且，index 变量也在相同优先级元素比较的时候起到重要作用。
        self._index += 1

    def pop(self):
        # 总是返回 ”最小的” 的元素
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

    # 如果以元组 (priority, item)的形式来表示元素，只要两个元素的优先级不同就能比较。
    a = (1, Item('foo'))
    b = (2, Item('bar'))
    print(a > b)

    # 但是如果两个元素优先级一样的话，那么比较操作就会出错
    c = (1, Item('grok'))
    # print(a > c)

    # 通过引入另外的 index 变量组成三元组 (priority, index, item) ，就能很好的避免上面的错误
    a = (1, 0, Item('foo'))
    c = (1, 1, Item('grok'))
    print(a > c)
