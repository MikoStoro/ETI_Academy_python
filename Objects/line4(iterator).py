from typing import Any


class Series:
    def __init__(self, function, start = 0, end = 10, step = 1):
        self._function = function
        self._start = start
        self._end = end
        self._step = step
        self._current = self._start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current <= self._end:
            value = self._function(self._current)
            curr = self._current
            self._current += self._step
            return {curr : value}
        else:
            raise StopIteration
    
    

class LinearFunction:
    def __init__(self, a = 1, b = 0, name = "Linear function"):
        self.a = a
        self.b = b
        self.name = name
    
    def _value(self, x):
        return self.a * x + self.b
    
    def __call__(self, x):
        return self._value(x)
    
    def __str__(self) -> str:
        return self.name + ": " + str(self.a) + "x + " + str(self.b)
    
    
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
    
    def getSeries(self, start = 0, end = 10, step = 1):
        for val in Series(function=self, start=start, end=end, step=step):
            yield val
    
    

f1 = LinearFunction(2,3, "f1")
print(f1)
print(f1(2))
f2 = f1 + 3
print(f2(2))
f3 = f1 * 2
print(f3(2))

for val in Series(f1, step=0.25):
    #print(val)
    pass
    
for val in f1.getSeries(step = 0.33):
    print(val)