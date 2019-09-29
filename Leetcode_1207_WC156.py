"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences
of each value in the array is unique.

Example:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

# SOLUTION
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
    
        freq = Counter(arr)
        return len(freq) == len(set(freq.values()))



