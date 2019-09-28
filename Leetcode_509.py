"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that
each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).

Example 1:
F(4) = F(3) + F(2) = 2 + 1 = 3.
"""

#SOLUTION

import numpy as np

class Fibonnaci_Number:
#   RECURSIVE
    def fib_rec(self, N: int) -> int:
         if fib_ar[i] <= 1:
             return N
         else:
             return self.fib(N-1) + self.fib(N-2)
        
#   DYNAMIC - USING NUMPY
    def fib_dyn_numpy(self, N: int) -> int:
         if N <= 1:
             return N
         fib_ar = np.arange(N+1)
        
         fib_ar[0] = 0
         fib_ar[1] = 1
        
         sol = 0
         for i in range(2,N+1,1):
             fib_ar[i] = fib_ar[i-1] + fib_ar[i-2]
             sol = fib_ar[i]        
         return sol

#    DYNAMIC - WITH ARRAY
     def fib_dyn_arr(self, N: int) -> int:
         if N <= 1:
             return N
        
         fib_ar = [0,1]
        
         sol = 0
         for i in range(2,N+1,1):
             fib_ar.append(fib_ar[i-1] + fib_ar[i-2])
             sol = fib_ar[i]
         return sol
         
#    DYNAMIC - NO ARRAY     
     def fib_dyn(self, N: int) -> int:
         if N <= 1:
             return N
             
         n_1 = 0
         n_2 = 1

         for i in range(2,N+1,1):
             N_f = n_1 + n_2
             n_1 = n_2
             n_2 = N_f

         return N_f
