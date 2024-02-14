import matplotlib.pyplot as plt 
import numpy as np


rnd_f = open('abc_data.csv', 'r')
rnd = rnd_f.read().split(';')
rnd_f.close()
#rnd = [ord(x) for x in rnd]
plt.hist(rnd, 3)
plt.show()

rnd_2=[ sum( (x=='a') for x in rnd), sum( (x=='b') for x in rnd),  sum( x=='c' for x in rnd)]
#rnd_2 = [int(x) for x in rnd_2]
print(rnd_2)
plt.pie(rnd_2, labels=['a','b','c'])
plt.show()

