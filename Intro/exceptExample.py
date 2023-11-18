import numbers


class ZeroDivision(BaseException):
    pass

class NotInt(BaseException):
    def __init__(self, value="value"):
        print("ERROR: " + str(value) +  " is not a number")
        super().__init__()

def divide(dzielna, dzielnik):
    if not isinstance(dzielna, int):
        raise NotInt(dzielna)
    if not isinstance(dzielnik, int):
        raise NotInt(dzielnik)
    if dzielnik == 0:
        raise ZeroDivision()
    return dzielna/dzielnik

def epicFunction(x,y):
    return divide(x,y)

print(epicFunction(1,2))
try:
    print(divide("1",2))
except BaseException:
    pass
try:
    print(epicFunction(2,0))
except NotInt:
    pass

