from collections import deque
from fractions import Fraction
import sys
import random
import operator as op
# from anytree import Node, RenderTree
from numpy.polynomial.polynomial import Polynomial as Poly
import numpy as np
from scipy.special import comb
from scipy import optimize

# convert an assignment to polynomial
# L is the left half tree assignment of the upper tree
def assign_to_poly(L, R):
 
    # left tree node selected to be 0
    D = [i + 1 for i in range(len(L)) if L[i] == 0]
    
    # right tree node selected to be 0
    E = [i + 1 for i in range(len(R)) if R[i] == 0]
    
    #left tree node selected be to be 1
    F = [i + 1 for i in range(len(L)) if L[i] == 1]
    
    # right tree node selected to be 1
    G = [i + 1 for i in range(len(R)) if R[i] == 1]
    
    poly_zero = Poly(np.zeros(1, dtype=int))
    poly_one = Poly(np.zeros(1, dtype=int))
    poly_p = Poly(np.array([0, 1], dtype=np.int))
    poly_q = Poly(np.array([1, -1], dtype=np.int))
    
    for i in D:
        poly_zero += poly_p ** i * poly_q
        
    for i in E:
        poly_zero += poly_p * poly_q ** i
        
    for i in F:
        poly_one += poly_p ** i * poly_q
    
    for i in G:
        poly_one += poly_p * poly_q ** i

    # this section is used to compute the extrema

    # x = [-int(e) for e in poly_zero.coef]
    # y = [-int(e) for e in poly_one.coef]
    # x.reverse()
    # y.reverse()

    # f_x = np.poly1d(x)
    # f_y = np.poly1d(y)

    # result = optimize.fmin(f_x, 0, disp=False)
    # p_zero = -f_x(result[0])
    # if p_zero > 0.5: return

    # result = optimize.fmin(f_y, 0, disp=False)
    # p_one = -f_y(result[0])
    # if p_one > 0.5: return


    return (poly_zero, poly_one)
    # print (L, R)

poly = assign_to_poly([0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0])

from print_poly import print_poly

print_poly(poly[0].coef)
print_poly(poly[1].coef)

