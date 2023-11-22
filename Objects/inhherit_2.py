class Class1():
    def display(self):
        print("class1")


class Class2(Class1):
    def display(self):
        print("class2")
        super().display()

class Class3(Class2):
    def display(self):
        print("class3")
        super().display()



obj3 = Class3()
obj3.display()

obj2 = Class2()

print("is instance?")
print(isinstance(obj2, Class2))
print(isinstance(obj2, Class1))

print("inherits?")
print(issubclass(Class2, Class2))
print(issubclass(Class2, Class1))
