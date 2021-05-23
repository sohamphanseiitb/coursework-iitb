import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 510, 511)
mesh = time[1] - time[0]
velocity = 0*np.ones(511)
height = -8*np.ones(511)
m_0 = 2094060
g_0 = 9.81
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

def m(t):
    if t<tb1:
        return m_0 - (beta_srb + beta_ssme)*t
    elif t>=tb1 and t<tb2:
        return m_0 - m_p_srb - beta_ssme*t - m_struct_srb
    elif t>=tb2:
        return m_0 - m_p_srb - m_p_ssme - m_struct_srb - m_struct_et

def dmdt(t):
    if t<tb1:
        return -1*(beta_srb + beta_ssme)
    elif t>=tb1 and t<tb2:
        return -1*beta_ssme
    elif t>=tb2:
        return 0

def dvdt(t):
    return (-dmdt(t)/m(t))*g_0*((beta_srb*Isp_srb + beta_ssme*Isp_ssme)/(beta_srb + beta_ssme)) - g_0

#def dvdt(t):
    #if t<=tb1:
    #    return ((g_0/m(t))*(beta_srb*Isp_srb + beta_ssme*Isp_ssme)) - g_0
    #elif t>tb1 and t<=tb2:
    #    return ((g_0/m(t))*(beta_ssme*Isp_ssme)) - g_0

def v(t):
    if t==0:
        return velocity[0]
    if velocity[int(t)]==0:
        velocity[int(t)] = v(t-mesh) + mesh*dvdt(t-mesh)
    else:
        return velocity[int(t)]
    return velocity[int(t)]

def dhdt(t):
    return v(t)

def h(t):
    if t==0:
        return height[0]
    if height[int(t)]==0:
        returnvalue = v(t-mesh) + mesh*dhdt(t-mesh)
        height[int(t)] = returnvalue
    else:
        return height[int(t)]
    return returnvalue

for t in time:
    v(t)
    h(t)

#print(velocity)
print(dvdt(t))
plt.plot(time, velocity)
plt.show()
