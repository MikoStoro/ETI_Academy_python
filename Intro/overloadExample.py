# z jednym parametrem uznajemy, że to kwadrat
# jeśli argumentów jest więcej, to uznajemy  
def rectangleArea(a, b = None, **args):
    if b is None:
        b = a
    return a*b

print(rectangleArea(2))
print(rectangleArea(2,3))
print(rectangleArea(2, c = 1))


def printArgs(example = None, **args):
    for arg in args:
        print(arg, args[arg])

printArgs(456, a = 1, b = 2, c = 3) 