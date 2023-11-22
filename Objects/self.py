class OBJ:
    x = 10

    def add_and_print(self):
        self.x += 1
        print(self.x)


o1 = OBJ()
o1.add_and_print()

OBJ.add_and_print(o1)

##Możemy zmienić nazwę "self", i tak zadziała