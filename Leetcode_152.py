"""
Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

# SOLUTION by lee215
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        front, back = nums, nums[::-1]
        
        for i in range(1,len(nums)):
            front[i] = front[i] * (front[i-1] or 1)
            back[i] = back[i] * (back[i-1] or 1)

        return max(front + back)

# EXPLANATION

# multiple subarrays from beginning to end in one array and multiply subarrays from end to beginning in another array.
# This is becacuse if you have [-1,-2,-100] then subaeeay is [-1,2,-200] but the inverse array [-100,-2,-1] will yield
# [-100,200,-200] since the smallest negative value becomes the largest when multiplied by the largest negative.
# NOTE: make sure to start from index 1 in order to maintain the index 0 unchanged.
# If in any of the multiplications there is a zero then reset the subarray value to 1 in order to start a new subarray.
# Concatenate both array together and return the largest contigous array.
