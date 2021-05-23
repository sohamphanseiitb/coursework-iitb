import numpy as np
import matplotlib.pyplot as plt

x = np.array([6.394884621840902e-14, 19.772727272727337,49.54545454545459,76.59090909090912,107.04545454545456,114.0909090909091,120.90909090909088,125.68181818181816])
y = np.array([2773257.57575758,3039848.484848491,2236439.393939401,2538787.878787889,1702272.727272739,757954.5454545561,186893.9393939497,55151.51515152585])

y_n = y * 4.44822

Isp = 242
g0 = 9.81

beta = y_n/(Isp*g0)

area = np.trapz(beta, dx = 10000)
print(area)


#plt.plot(x, y, label="Individual SRB Data in LBF",)
#plt.plot(x, y_n, label="Individual SRB Data in N")
plt.plot(x, beta, label='Data Based Simplified Burn Rate in kg/s')
#plt.plot(x, y, 'ro')
#plt.plot(x, y_n, 'bx')
plt.plot(x, beta, 'go')
plt.plot(x, 3937.0078*np.ones(np.size(x)), 'r', label="Constant Burn Rate Assumption")
plt.title("Simplified Burn Rate Profile of Solid Rocket Booster")
plt.xlabel("Mision Elapsed Time (in seconds)")
plt.ylabel("Burn Rate in kg/s")
plt.grid(True)
plt.xlim((0, x[-1]))
plt.ylim(0)
plt.legend(loc="best")
plt.show()
