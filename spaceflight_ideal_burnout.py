#AE240 Spaceflight Mechanics
#Author - Soham S. Phanse
#Department of Aerospace Engineering, IIT Bombay
import numpy as np
import matplotlib.pyplot as plt
import math as m

# Ideal Burnout performance
## Consider vertical trajectory with no gravity and drag
## Burn profile - constant burn profile
#------------------------------------------------------
m_p = 60*(10**3)      ### mass of propellant
m_star = 0   ### mass of payload
m_s = None      ### mass of structure
m_0 = 80*(10**3)      ### mass at take-off
m_b = m_0 - m_p ### mass at burnout
payload_ratio = m_star/m_0
structure_ratio = 0
propellant_ratio = m_p/m_0
Burnout_ratio = 1 - propellant_ratio
beta = 600     ### Burn rate of propellant
t_b = m_p/beta  ### Burnout time
t_s = 0         ### start time
t_e = t_b       ### end time
t = np.linspace(t_s, t_e, 100) ### time array of values
g_0 = 9.81      ### standard value of gravity
I_sp = 240      ### specific impulse value of propellant
V_0 = 0         ### Velocity at take-off
R_earth = 6371  ### Radius of earth

def ideal_burnout(time):
    m_t = m_0 - beta*time
    V_ideal_t = V_0 + g_0*I_sp*(m.log(m_t/m_0))  ### Velocity at time t
    return m_t, V_ideal_t

#-------------------------------------------------
V_ideal_burnout = V_0 + g_0*I_sp*(m.log(m_b/m_0))
mass, velocity = [], []
for each in t:
    store = ideal_burnout(each)
    mass.append(store[0])
    velocity.append(abs(store[1]))

#plt.plot(t, velocity, label="Ideal Burnout Velocity")
#plt.plot(t_b, abs(V_ideal_burnout), 'ro')
#plt.xlabel("Time \u2193")
#plt.ylabel("Velocity \u2193")
#plt.xlim(0)
#plt.title("Ideal Burnout performance")
#plt.legend()
#plt.show()

# Assuming gravity , we get the following expressions for velocity and altitude gained
#----------------------------------------------------------
g_avg = g_0
mass_g, velocity_g, altitude_g = [], [], []
def gravity_burnout(time):
    m_t = m_0 - beta*time
    V_gravi_t = g_0*I_sp*m.log(m_0/m_t) - g_avg*time
    H_gravi_t = g_0*I_sp*time*(1 + m.log(m_0/m_t)) + (m_0*g_0*I_sp)*m.log(m_t/m_0)/beta - g_avg*time**2/2 + V_0*time
    return m_t, H_gravi_t, V_gravi_t

for each in t:
    store = gravity_burnout(each)
    mass_g.append(store[0])
    altitude_g.append(store[1])
    velocity_g.append(store[2])

V_gravi_burnout = g_0*I_sp*m.log(m_0/m_b) - g_avg*t_b
H_gravi_burnout = g_0*I_sp*t_b*(1 + m.log(m_0/m_b)) + (m_0*g_0*I_sp)*m.log(m_b/m_0)/beta - g_avg*t_b**2/2 + V_0*t_b

plt.plot(t, velocity_g, label="Velocity under gravity burnout")
plt.plot(t, velocity, label="Velocity under ideal burnout")
#plt.plot(t, altitude_g, label="Altitude under gravity burnout")
plt.plot(t_b, abs(V_gravi_burnout), 'ro', label="Burnout velocity under gravity")
plt.plot(t_b, abs(V_ideal_burnout), 'bo', label="Ideal Burnout velocity")
plt.plot(t_b, 0,'go', label="Burnout Time")
plt.xlabel("Time \u2193")
plt.ylabel("Velocity \u2193")
plt.xlim(0)
plt.ylim(0)
plt.title("Gravity Burnout performance")
plt.legend()
plt.show()

# Solution update: Update the g according to the old altitude,
# according to new g update the velocity and altitude.
g_new = g_0/(1 + H_gravi_burnout/R_earth)**2
g_updated = (g_0 + g_new)/2
V_gravi_burnout_updated = g_0*I_sp*m.log(m_0/m_b) - g_updated*t_b
H_gravi_burnout_updated = g_0*I_sp*t_b*(1 + m.log(m_0/m_b)) + (m_0*g_0*I_sp)*m.log(m_b/m_0)/beta - g_updated*t_b**2/2 + V_0*t_b
