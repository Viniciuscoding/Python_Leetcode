"""
Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.


Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.
"""

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # MY SOLUTION
#         arr_in = []
#         arr_out = []
        
#         for v2 in arr2:
#             for v1 in arr1:
#                 if v2 == v1:
#                     arr_in.append(v1)

#         [arr_out.append(i) for i in arr1 if i not in arr2]

#         return arr_in + arr_out.sort()
        
        # SOLUTION BY lee215 (2x fast)
        arr2_list = {v2: i for i, v2 in enumerate(arr2)}
        return sorted(arr1, key=lambda v1: arr2_list.get(v1, 1000 + v1))
