class Counter:
    x = 0

    def add(self):
        self.x += 1

    def getCount(self):
        print(self.x)
    
    def display(self):
        print(self.x)

class TwoWayCounter(Counter):

    def sub(self):
        self.x -= 1

class BackwardCounter(TwoWayCounter):
    def add(self):
        pass

counter = TwoWayCounter()

print("Counter:")
counter.sub()
counter.display()
counter.add()
counter.add()
counter.add()
counter.display()

counter2 = Counter()
# nie zadziała
#counter2.sub()

counter3 = BackwardCounter()
print("Backward counter")
counter3.display()
counter3.add()
counter3.display()
counter3.sub()
counter3.display()

     