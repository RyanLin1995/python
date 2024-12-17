# 在很多程序中，有些对象会根据状态的不同来执行不同的操作。比如考虑如下的一个连接对象：
class Connection:
    """普通方案，好多个判断语句，效率低下~~"""

    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('reading')

    def write(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('writing')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already open')
        self.state = 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed')
        self.state = 'CLOSED'


# 一个更好的办法是为每个状态定义一个对象：
class Connection1:
    """新方案——对每个状态定义一个类"""

    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate
        # Delegate to the state class

    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


# Connection state base class
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()


# Implementation of different states
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


# 第二种写法
class Connection2:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, new_state):
        self.__class__ = new_state

    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


class ClosedConnection(Connection2):
    def read(self):
        raise RuntimeError('Not open')

    def write(self, data):
        raise RuntimeError('Not open')

    def open(self):
        self.new_state(OpenConnection)

    def close(self):
        raise RuntimeError('Already closed')


class OpenConnection(Connection2):
    def read(self):
        print('reading')

    def write(self, data):
        print('writing')

    def open(self):
        raise RuntimeError('Already open')

    def close(self):
        self.new_state(ClosedConnection)


# 示例二
# Original implementation
class State:
    def __init__(self):
        self.state = 'A'

    def action(self, x):
        if self.state == 'A':
            # Action for A
            ...
            self.state = 'B'
        elif self.state == 'B':
            # Action for B
            ...
            self.state = 'C'
        elif self.state == 'C':
            # Action for C
            ...
            self.state = 'A'


# Alternative implementation
class State1:
    def __init__(self):
        self.new_state(State_A)

    def new_state(self, state):
        self.__class__ = state

    def action(self, x):
        raise NotImplementedError()


class State_A(State1):
    def action(self, x):
        # Action for A
        ...
        self.new_state(State_B)


class State_B(State1):
    def action(self, x):
        # Action for B
        ...
        self.new_state(State_C)


class State_C(State1):
    def action(self, x):
        # Action for C
        ...
        self.new_state(State_A)


# 设计模式中有一种模式叫状态模式，这一小节算是一个初步入门！

if __name__ == '__main__':
    # c = Connection1()
    # print(c._state)
    # print(c.read())
    # print(c.open())
    # print(c._state)
    # print(c.read())
    # print(c.write('hello'))
    # print(c.close())
    # print(c._state)

    c = Connection2()
    print(c)
    print(c.read())
    print(c.open())
    print(c)
    print(c.read())
    print(c.write('hello'))
    print(c.close())
    print(c)
