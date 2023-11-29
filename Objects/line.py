class LinearFunction:
    def __init__(self, a = 1, b = 0):
        self.a = a
        self.b = b
    
    def value(self, x):
        return self.a * x + self.b
    
    def __add__(self, other):
        newFun = LinearFunction(self.a, self.b)
        
        if(isinstance(other, float) or isinstance(other, int)):
            newFun.b += other
            return newFun
        
        if(isinstance(other, LinearFunction)):
            newFun.a += other.a
            newFun.b += other.b
            return newFun
        
        raise TypeError()
    
    def __mul__(self, other):
        newFun = LinearFunction(self.a, self.b)
        if(isinstance(other, float) or isinstance(other, int)):
            newFun.b *= other
            newFun.a *= other
            return newFun
        raise TypeError()
    
    def __truediv__(self, other):
        newFun = LinearFunction(self.a, self.b)
        if(isinstance(other, float) or isinstance(other, int)):
            newFun.b /= other
            newFun.a /= other
            return newFun
        raise TypeError()
    

f1 = LinearFunction(2,3)
print(f1.value(2))
f2 = f1 + 3
print(f2.value(2))
f3 = f1 * 2
print(f3.value(2))