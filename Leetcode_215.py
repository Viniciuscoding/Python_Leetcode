"""
Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # SOLUTION descending order (A little faster since it is unecessary to find the length of the array)
        sort_desc_nums = sorted(nums, reverse = True)
        return sorted_nums[k - 1]
        
        # SOLUTION ascending order
        sort_asc_nums = sorted(nums)
        return sorted_nums[len(nums) - k]

# EXPLANATION
# 1. Sort the array in descending order.
# 2. Return the value at the index of the kth value. Keep in mind Python index starts at zero, so k must be subtracted by 1.
# 3. You can also sove by sorting in ascending order. When you do that you have to find the kth position from the end to the
#    the beginning by subtracting the array length with the kth value. Then return that index value.
