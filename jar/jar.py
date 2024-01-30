class Jar:
    def __init__(self, capacity=12, size=0):
        self._capacity = capacity
        self._size = size
        if self.capacity < 0:
            raise ValueError

    def __str__(self):
        n = self.size
        cookies = ""
        i = 0
        while i < n:
            cookies += "🍪"
            i += 1
        return cookies

    def deposit(self, n):
        total = self.size + n
        if total <= self.capacity:
            self.size = total
        else:
            raise ValueError

    def withdraw(self, n):
        m = self.size - n
        if m < 0:
            raise ValueError
        else:
            self.size = m

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if self.capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter # initiate the value of size here
    def size(self, value=0):
        self._size = value
