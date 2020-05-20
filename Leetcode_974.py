"""
Subarray Sums Divisible by K



"""

class Solution(object):
    def subarraysDivByK(self, A, K):
        # MY SOLUTION - Brute Force
        s = len(A)
        beg, end = 0, 1
        brek = 1
        count = 0
        
        while brek <= len(A):
            if sum(A[beg:end]) % K == 0:
                count += 1
            beg += 1
            end += 1
            if end > len(A):
                brek += 1
                beg = 0
                end = brek
        return count
        
        # SOLUTION from Leetcode fastest
        res, prefix = 0, 0
        count = [1] + [0] * (K-1)
        for a in A:
            prefix = (prefix + a) % K
            res += count[prefix]
            count[prefix] += 1
        return res
