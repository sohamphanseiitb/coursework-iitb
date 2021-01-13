#Author: Soham S. Phanse, II yr UG
# Department of Aerospace Engineering, IIT Bombay
# As a part of course on MA214 - Numerical Analysis
## Spring 2021
#This code calculates the lagrange polynomials and the interpolant
import numpy as np
import matplotlib.pyplot as plt

data = np.array([-1,0,0.5,1])
values = np.array([1,0,0.25,1])

#The ith lagrange polynomial generating function
def lagrange(x, i):
    product_num, product_den = 1, 1
    for j in range(len(data)):
        if j!=i:
            product_num = product_num*(x-data[j])
            product_den = product_den*(data[i]-data[j])
    return product_num/product_den

# The interpolant function as a weighted linear combination of lagrange Polynomials
def interpolant(x):
    sum = 0
    for k in range(len(data)):
        sum = sum + values[k]*lagrange(x,k)
    return sum

x = np.linspace(-1,1,500)
for l in range(len(data)):
    plt.plot(x, lagrange(x,l), label="lagrange_poly" + str(l))
plt.plot(x, interpolant(x), label="interpolant")
plt.plot(data, values, "ro")
plt.xlabel("Data Points (Arguments)")
plt.ylabel("Function Values")
plt.legend()
plt.grid()
plt.show()
