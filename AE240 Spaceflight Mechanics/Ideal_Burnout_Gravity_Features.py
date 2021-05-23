#AE240 Spaceflight Mechanics/
#Author - Soham S. Phanse
#Department of Aerospace Engineering, IIT Bombay
import numpy as np
import matplotlib.pyplot as plt
import math as m

m_0, m_p, beta, beta2, I_sp, g_0, V_0 = 80*(10**3), 60*(10**3), 600, 300, 240, 9.81, 0

def t_b(m_p, beta):
    return m_p/beta

time = np.linspace(0, t_b(m_p, beta), 100)
def ideal_burnout(time, beta, V_0, g_0, I_sp, m_0):
    m_t = m_0 - beta*time
    V_ideal_burnout = V_0 + g_0*I_sp*(m.log(m_t/m_0))
    return m_t, V_ideal_burnout

def gravity_burnout(time, beta, V_0, g_0, I_sp, m_0):
    m_t = m_0 - beta*time
    g_avg = g_0
    V_gravi_t = g_0*I_sp*m.log(m_0/m_t) - g_avg*time
    H_gravi_t = g_0*I_sp*time*(1 + m.log(m_0/m_t)) + (m_0*g_0*I_sp)*m.log(m_t/m_0)/beta - g_avg*time**2/2 + V_0*time
    return m_t, V_gravi_t, H_gravi_t

#Ideal Energy
Energy_ideal = 0
store2 = ideal_burnout(time, beta, V_0, g_0, I_sp, m_0)
Energy_ideal = 0.5*store2[0]*(store2[1]**2)

def energy_gravity_burnout(time, beta, V_0, g_0, I_sp, m_0):
    store = gravity_burnout(time, beta, V_0, g_0, I_sp, m_0)
    Energy_gravity = 0.5*store[0]*(store[1]**2) + (store[0]*g_0*store[2])
    return Energy_gravity

for each in time:
    Energy_gravity_beta  = energy_gravity_burnout(each, beta, V_0, g_0, I_sp, m_0)
    Energy_gravity_beta2 = energy_gravity_burnout(each, beta2, V_0, g_0, I_sp, m_0)

plt.plot(time, Energy_ideal, label="Mechanical Energy Ideal Burnout")
plt.plot(time, Energy_gravity_beta, label="Mechanical Energy Gravity Burnout Beta = " + str(beta))
plt.plot(time, Energy_gravity_beta2, label="Mechanical Energy Gravity Burnout Beta = " + str(beta2))
plt.title("Mechanical Energy Comparison with Beta")
plt.xlim(0)
plt.ylim(0)
plt.legend()
plt.show()
