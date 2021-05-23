import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 520, 27)
altitude = np.array([-8, 1244, 5377, 11617, 19872, 31412, 44726, 57396, 67893, 77485, 85662, 92481, 98004, 102301, 105321, 107449, 108619, 108942, 108543, 107690, 106539, 105142, 103775, 102807, 102552, 103297, 105069])
velocity = np.array([0, 139, 298, 433, 685, 1026, 1279, 1373, 1490, 1634, 1800, 1986, 2191, 2417, 2651, 2915, 3203, 3516, 3860, 4216, 4630, 5092, 5612, 6184, 6760, 7327, 7581])
acceleration = np.array([2.45, 18.62, 16.37, 19.40, 24.50, 24.01, 8.72, 9.70, 10.19, 10.68, 11.17, 11.86, 12.45, 13.23, 13.92, 14.90, 15.97, 17.15, 18.62, 20.29, 22.34, 24.89, 28.03, 29.01, 29.30, 29.01, 0.1])

test = velocity/9.81
y = 0.0005  #Time avergaed rate -- 90 degrees/ 510 seconds == 0.003079992
rhs = np.sin(y*time)/y

'''
Constant Pitch Rate Solution -
We have time of ascent =  510 seconds
Change in pitch angle = 90 degrees
Pitch Rate q_0 = 0.003079992 degrees per second
So we velocity -- V(t) = \frac{g_0*sin(theta(t))}{q_0}
'''
q_0, theta_0, g_0, h_0, x_0 = 0.00307992, 0, 9.81, -8, 0
def altipitch(t):
    return ((g_0/(4*q_0**2))*(np.cos(2*theta_0) - np.cos(2*theta(t)))) + h_0
def rangepitch(t):
    return ((g_0/(2*q_0**2))*(((180/np.pi)*(theta(t)-theta_0)) - ((np.sin(2*theta(t))-np.sin(2*theta_0))*0.5))) + x_0
def theta(t):
    return q_0*t + theta_0
def vpitch(t):
    return g_0*np.sin(theta(t))/q_0

time = np.linspace(0, 510, 1021)
for t in time:
    print(vpitch(t))
#-------------------------------------------------------------------------------
#plt.plot(time, velocity)
#plt.plot(time, rhs)
plt.show()
