# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 08:33:26 2020

@author: Matt
"""

# from itertools import product
from math import factorial

class Expect():
    def __init__(self):
        self.omega = set()
        self.outcomes = list()
        self.probs = list()
        self.expect = 0
        
    def q2(self):
        for i in range(1, 7):
            for j in range(1,7):
                print(i,j,i*j)
                self.omega.add(i*j)
                self.outcomes.append(i*j)
                
        for X in list(self.omega):
            n=0
            for Y in self.outcomes:
                if X == Y: n+=1
            self.probs.append(n/len(self.outcomes))
            
        for i in range(0, len(self.omega)):
              self.expect += list(self.omega)[i]*self.probs[i]
        return(self.expect, list(self.omega))
    
    def q3(self):
        Z = list(range(1,7))
        
        for X in Z:
            if X % 2 == 0: 
                self.omega.add(3*X)
                self.outcomes.append(3*X)
            else: 
                self.omega.add(-4*X)
                self.outcomes.append(-4*X)
        
        for X in self.omega:
            n=0
            for Y in self.outcomes:
                if X == Y: n+=1
            self.probs.append(n/len(self.outcomes))
            
        return 1/6*sum(self.omega)
        for i in range(0, len(self.omega)):
            self.expect += list(self.omega)[i]*self.probs[i]
        return(self.expect, list(self.omega))
    
    def q4(self): #?? something is off here
        # m = 0
        # n = 0
        # self.omega = set(product(range(1,7), repeat=6))
        # for X in self.omega:
            # k = 0
            # for i in range(0,5):
            #     if X[i] != X[i+1] and X[5] != X[0]:
            #         k += 1
            # if k == 5: m += 1
            # else: n+=1
            
            # z=0
            # for i in range(6):
            #     l=0
            #     for j in range(6):
            #         if X[i] != X[j]:
            #             l+=1
            #     if l == 6:
            #         print(X)
            #         z+=1
                    
        # return (m,z,n)
        
        return (factorial(6)/6**6)*-60+(6**6-120)/6**6
    
    def test(self,X):
        m=0
        n=0
        k=0
        for i in range(0,3):
            if X[i] != X[i+1]:
                k += 1
                print(k)
        if k == 2: m += 1
        else: n+=1
        return (m,n)
              
        
        