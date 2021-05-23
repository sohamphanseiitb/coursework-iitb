import numpy as np
import matplotlib.pyplot as plt

#theta_0 = np.arange(0, np.pi*0.5, np.pi/360)
#RHS = np.pi*0.5 - theta_0
#LHS = 3.695484369*np.sin(theta_0)
#plt.plot(theta_0, RHS)
#plt.plot(theta_0, LHS)
#plt.plot(0.338, 1.24, 'rx')
#plt.xlabel('$theta_0$')
#plt.xlim(0)
#plt.title('Initial Angle Estimation')
#plt.annotate('theta_0', [0.338, 1.24])
#plt.legend(loc='best')
#plt.show()
theta_0 = np.arange(0, np.pi*0.5, np.pi/720)
q_0 = np.arange(0, 2.2659*0.00001, np.pi/720)
for each in theta_0:
    for every in q_0:
        theta_b = each + every*383
        x = np.sin(each)
        y = np.sin(theta_b)
        if abs(x - 0.1325*y)<=0.02 and theta_b<=np.pi*0.45:
            print(each, every)
