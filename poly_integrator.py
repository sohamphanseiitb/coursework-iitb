import numpy as np
import matplotlib.pyplot as plt
import math as m

# This function integrates only polynomials in an exact manner.
## The required data by the function is listed below:
## 1. End points of the domain: a: Lower Limit, b: Upper Limit
## 2. Polynomial array: Array of co-efficients of a polynomial arranged
## in ascending order of the degree of the terms. eg: x^0, x^1, x^2 and so on.

a, b = 0, 1
p = [5] #denotes p(x) = x in [0,1]

def find_val(parray, arg):
    sum, store = 0, 1
    d = len(parray) - 1
    for every in parray:
        degree = parray.index(every)
        sum = sum + every*(store)
        store = store*arg
    return sum


def poly_integrator(a,b,p):
    antider = [0]
    for each in p:
        degree = p.index(each)
        antider.append(each/(degree+1)) #This computes the array of co-efficients for the anit-derivative
        print(antider)
    return find_val(antider, b) - find_val(antider, a)

print(poly_integrator(a,b,p))
