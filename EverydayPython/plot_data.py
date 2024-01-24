from math import sin
import random as rnd

x = []
y = []
for i in range(0,200):
    curr_x = i * 0.05
    curr_y = sin(curr_x)
    x.append(str(curr_x))
    y.append(str(curr_y))
    print({curr_x:curr_y})

datafile = open('sinus_data.csv', 'w')
datafile.write(';'.join(x))
datafile.write('\n')
datafile.write(';'.join(y))
datafile.close()


abc = []
for i in range(500):
    chance = rnd.random()
    if chance < 0.1:
       abc.append('a')
    elif chance < 0.4:
        abc.append('b')
    else:
        abc.append('c')
datafile = open('abc_data.csv', 'w')
datafile.write(';'.join(abc))
datafile.close()