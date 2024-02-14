import matplotlib.pyplot as plt 

##SINUS
sinus_f = open('sinus_data.csv','r')
sinus = sinus_f.read().split('\n')
sinus_f.close()
x = [float(x) for x in sinus[0].split(';') ]
y = [float(x) for x in sinus[1].split(';') ] 

plt.plot(x,y)
#plt.xlabel('oś x')
#plt.ylabel('oś y')
#plt.axis([3.14,6.28,-1.25,1.25])   
plt.show()