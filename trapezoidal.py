# MA214 - Numerical Analysis, Spring 2021
# Author - Soham S. Phanse
# Department of Aerospace Engineering, IIT Bombay
import numpy as np
import matplotlib.pyplot as plt

# Here, we solve a simple differential equation using the trapezoidal method.
# y' = y with the initial condition y(0) = 1
# Here, we have the recurrence relation as y(n+1) = (2+h)*y(n)/(2-h)
# We will solve it in a domain [0,1] and plot the solution we get with varying
## number of mesh points.
a, b, N = 0, 1, 100
global_mesh = 0
def plot_data_supply(a,b,N):
    h = (b-a)/N
    mesh_args = np.linspace(a,b,N+1)
    y_vals = [1] # Initial condition is same
    for i in range(1,N+1):
        pass
        y_vals.append((2+h)*(y_vals[i-1])/(2-h)) # This recurrence relation is unique to the differential equation under consideration
    return mesh_args, y_vals, np.exp(mesh_args)

for each in range(1,6,1):
    print(each)
    store = plot_data_supply(a,b,each)
    global_mesh = store[0]
    #plt.plot(store[0], store[1], label= str(each))
    # Absolute error in the approximations
    plt.plot(store[0], abs(store[1] - store[2]), label="Error" + str(each))
    plt.xlim(0,1)

#plt.plot(store[0], store[2], label="Exponential")
plt.legend()
plt.show()
