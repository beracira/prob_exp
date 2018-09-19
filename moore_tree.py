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

# check the necessary probability condition
# L is the left half tree assignment of the upper tree
def prob_cond(L):
    E = Fraction(0, 1)
    p = Fraction(int(sys.argv[1]), 100)
    q = 1 - p
    
    # tree assignment
    # L = [0, 1, 1, 0, 1, 0, 0, 1]
    R = [1 - node for node in L]
    
    # left tree node selected to be 0
    D = [i + 1 for i in range(len(L)) if L[i] == 0]
    
    # right tree node selected to be 0
    E = [i + 1 for i in range(len(R)) if R[i] == 0]
    
    # print (D, E)
    
    # sum of the first equation
    first_sum = 0
    
    #sum of the second equation
    sec_sum = 0
    
    for i in D:
        first_sum += p ** i * q
        sec_sum += p * q ** i
        
    for j in E:
        first_sum += p * q ** j
        sec_sum += p ** j * q

    if first_sum <= 0.5 and sec_sum <= 0.5:
        print (L)
        return True
    else:
        return False
    # print (first_sum)
    # print (sec_sum)
    # print (float(first_sum))
    # print (float(sec_sum))


prob_cond([0,1,0,1,0,1,0,1,0])
