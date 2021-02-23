# MA214 - Numerical Analysis, Spring 2021
# Author - Soham S. Phanse
# Department of Aerospace Engineering, IIT Bombay
import numpy as np
import matplotlib.pyplot as plt

# This program will try and numerically approximate the integral of a function
# with the Simpson's 1/3 rule. This method can accurately determine integrals of
# polynomials upto degree 2 since it is 2nd ORDER method.

# We first describe end points.
a, b = 0, 1

# Then describe the forcing fucntion
def f(arg):
    return arg**2 + arg + 1

def simpson(a,b,f):
    return (b-a)*(f(a) + 4*f((a+b)/2) + f(b))/6

def compo_simpson(a,b,f,m):
    mesh = np.linspace(a,b,m)
    sum = 0
    for i in range(m-1):
        store = simpson(mesh[i],mesh[i+1],f)
        sum = sum + store
    return sum

print(simpson(a,b,f))
print(compo_simpson(a,b,f,3))
