print("LETTER SIZE")
string = "aBcDeF"
print(string)
print(string.lower())
print(string.capitalize())
print(string.upper())

print("\n\nSTRIP")
string= "  \n  abcdef  \n"
print(string)
print(string.strip())

print("\n\nSPLIT")
string = "a,b,c,d,e,f"
print(string)
print(string.split(','))

print("\n\nJOIN")
array = ['a','b','c','d','e','f']
print(array)
print(" ".join(array))

print("\n\nREPLACE")
string = "a,b,c,d,e,f"
print(string)
print(string.replace(',',' '))

print("\n\nINDEX")
string="abcdef"
print(string.find('cd'))
print(string.find('ac'))

print("\n\nFORMAT")
C = 36.6725
string="Temperature in celsius: {:f}, will we {:f} in Fahrenheit".format(C, (C*9/5)+32)
print(string)

print("\n\n\n")