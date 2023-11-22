class Ex1:
    pass
class Ex2:
    pass
class Ex3:
    pass

class SpecialClass(Ex1,Ex2,Ex3):
    x = 1
    y = 2
    z = 3
    def doc(self):
        """This Function
Does Nothing"""
        pass



item = SpecialClass()
print(item.__class__)
print(SpecialClass.__bases__)
print(SpecialClass.doc.__doc__)
print(print.__doc__)
print(SpecialClass.__dict__)
print(item.__sizeof__())
print([1,2,3,4].__sizeof__())
print([123,456].__sizeof__())