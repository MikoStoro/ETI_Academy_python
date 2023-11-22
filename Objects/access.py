class Example:
    public = 1
    _protected = 2
    __private = 3

class Example2:
    def __init__(self):
        self.public = 1
        self._protected = 2
        self.__private = 3


obj = Example()

##obj.__private = 123
#print(obj.__private)
print(obj._Example__private)


obj._protected = 123
print(obj._protected)


