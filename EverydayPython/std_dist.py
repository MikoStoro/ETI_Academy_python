import matplotlib.pyplot as plt 
import numpy as np


dist1 = np.random.standard_normal(10000)
plt.hist(dist1, 10)
plt.show()
plt.hist(dist1, 5)
plt.show()
