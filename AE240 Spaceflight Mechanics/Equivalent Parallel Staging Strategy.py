import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 510, 511)
m_0 = 2094060
g_0 = 9.81
v_0 = 0
h_0 = 0
tb1 = 127
tb2 = 510
m_p_srb = 1000000
m_p_ssme = 721897
Isp_srb = 255 #Averaged out value of atmosphere and vaccuum
Isp_ssme = 400 #Averaged out value of atmosphere and vaccuum
beta_srb = m_p_srb/tb1
beta_ssme = m_p_ssme/tb2
m_struct_srb = 180000
m_struct_et = 38103

beta = beta_srb + beta_ssme
Isp = (beta_srb*Isp_srb + beta_ssme*Isp_ssme)/beta
pi = (m_0 - m_struct_et - m_p_ssme - m_struct_srb - m_p_srb)/m_0
eps = (m_struct_et + m_struct_srb)/(m_struct_et + m_struct_srb + m_p_srb + m_p_ssme)

# Lets make a strategy of constant burn rate profile until burnout of SRBs
def m(t):
    return m_0 - beta_srb*t - beta_ssme*t

def dmdt(t):
    return (-beta_srb - beta_ssme)

def dvdt(t):
    return (-dmdt(t)/m(t))*(g_0*Isp) - g_0

def v(t):
    return (g_0*Isp)*(np.log(m_0/m(t))) - g_0*t

m_p = beta*tb1
l = m_p/m_0

def h(t):
    ((m_0*g_0*Isp)/beta)*((1-l)*np.log(1-l) + l) - ((0.5*g_0*l*l*m_0*m_0)/(beta*beta)) + (v_0*l*m_0)/beta + h_0

time = np.linspace(0, 127, 128)
velocity = []
altitude = []
mass = []
rate_change_mass = []
acceleration = []

for t in time:
    velocity.append(v(t))
    altitude.append(h(t))
    mass.append(m(t))
    rate_change_mass.append(dmdt(t))
    acceleration.append(dvdt(t))

plt.plot(time, velocity)
plt.grid(1)
plt.show()
