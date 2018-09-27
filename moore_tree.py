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

max_depth = int(sys.argv[1])

# check the necessary probability condition
# L is the left half tree assignment of the upper tree
def prob_cond(L, R):
 
    # tree assignment
    # L = [0, 1, 1, 0, 1, 0, 0, 1]
    # R = [1 - node for node in L]
    
    # left tree node selected to be 0
    D = [i + 1 for i in range(len(L)) if L[i] == 0]
    
    # right tree node selected to be 0
    E = [i + 1 for i in range(len(R)) if R[i] == 0]
    
    #left tree node selected be to be 1
    F = [i + 1 for i in range(len(L)) if L[i] == 1]
    
    # right tree node selected to be 1
    G = [i + 1 for i in range(len(R)) if R[i] == 1]
    
    # print (D, E, F, G)
    
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

    x = [-int(e) for e in poly_zero.coef]
    y = [-int(e) for e in poly_one.coef]
    x.reverse()
    y.reverse()

    f_x = np.poly1d(x)
    f_y = np.poly1d(y)

    result = optimize.minimize_scalar(f_x, bounds=(0, 1), method='bounded', options={'disp':False})
    p_zero = -f_x(result.x)
    if p_zero > 0.5: return

    result = optimize.minimize_scalar(f_y, bounds=(0, 1), method='bounded', options={'disp':False})
    p_one = -f_y(result.x)
    if p_one > 0.5: return


    if len(L) >= max_depth:
        # print (poly_zero, poly_one)
        print (L, R, p_zero, p_one)
        return
    prob_cond(L + [0], R + [0])
    prob_cond(L + [0], R + [1])
    prob_cond(L + [1], R + [0])
    prob_cond(L + [1], R + [1])




prob_cond([0], [1])

temp = (0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0)

a = []
b = []
for i in range(len(temp)):
    if i % 2 == 0:
        a += [temp[i]]
    else:
        b += [temp[i]]

print (a, b)