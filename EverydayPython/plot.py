import matplotlib.pyplot as plt 
import numpy as np


##SINUS
sinus_f = open('sinus_data.csv','r')
sinus = sinus_f.read().split('\n')
sinus_f.close()
x = [float(x) for x in sinus[0].split(';') ]
y = [float(x) for x in sinus[1].split(';') ] 

plt.plot(x,y)
#plt.axis([0,6,-0.5,0.5])   
plt.show()

rnd_f = open('abc_data.csv', 'r')
rnd = rnd_f.read().split(';')
rnd_f.close()
plt.hist(rnd, 3)
plt.show()

dist1 = np.random.standard_normal(10000)
plt.hist(dist1, 10)
plt.show()

rnd_2=[ sum( (x=='a') for x in rnd), sum( (x=='b') for x in rnd),  sum( x=='c' for x in rnd)]
#rnd_2 = [int(x) for x in rnd_2]
plt.pie(rnd_2, labels=['a','b','c'])
plt.show()