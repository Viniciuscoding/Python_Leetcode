"""
Subarray Sums Divisible by K

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 
Note:
1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
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
        
        # EXPLANATION
        # 1. Since the array is continuos, loop through all the continuous combinations possible.
        # 2. That was done by creating a while loop to go through all possible combinations and check everyone whose sum
        #    was divisible by K.
        # 2.1 Loop starts with one combination until the last combination includes all the elemements in the array. For example:
        # 2.2 Combination 1: [4] -> [5] -> [0] -> [-2] -> [-3] -> [1] then increase the combination to two
        # 2.3 Combination 2: [4, 5] -> [5,0] -> [0,-2] -> [-2,-3] -> [-3,1] then increase the combination to three
        #      ...
        # 2.4 Combination 5 (last one based on all the array elements): [4,5,0,-2,-3,1] then break the loop
        # 3. Return the count of combinations whose sum is divisible by K
        
        
        # SOLUTION from Leetcode fastest
        res, prefix = 0, 0
        count = [1] + [0] * (K-1)
        for a in A:
            prefix = (prefix + a) % K
            res += count[prefix]
            count[prefix] += 1
        return res
