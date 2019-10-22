"""
Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        zero, at = 0, 0
        count_0 = nums1.count(0)
        print(count_0)
        if zero in nums1:
            for i in range(len(nums1)):
                if nums1[i] == 0 and at < n:
                    nums1[i] = nums2[at]
                    at += 1
                if at == count_0:
                    break
        else:
            return nums1
        return nums1.sort()
