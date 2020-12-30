# -*- coding: utf-8 -*-

from itertools import product

# Conditional Proberbility

# Take the Cartesian product of {1,2} and {A,B,C}
list(product([1,2], ['A', 'B', 'C']))

n = 3 # number of coin tossings

omega = set(product(['H', 'T'], repeat=n)) # Sample space

A = {om for om in omega if om[0] == 'T'} # first tossing is tail
B = {om for om in omega if om.count('T') == 2}
C ={om for om in omega if om[1] == 'H'}

Z = {frozenset(A), frozenset(B), frozenset(C)}

W = {frozenset(A), frozenset(C)}

def prob(X):
    return len(X) / len(omega)

def cond_prob(X, Y):
    return len(X & Y) / len(Y)

class Are_indep:
    def pair(self, X,Y):
        return prob(X & Y) == prob(X) * prob(Y) # X & Y is union(X,Y)
    
    def coll(self, W):
        k=0
        for X in W: 
            for Y in W:
                if self.pair(X,Y) and X != Y: k+=1
        return k == len(W)
    