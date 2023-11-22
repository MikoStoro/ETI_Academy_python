class OBJ:
    x = 10

    def add(self):
        x+=1


o1 = OBJ()
o1.x = 123
o2 = OBJ()
o2.x = 123

print(o1==o2)
print(o1 is o2)
