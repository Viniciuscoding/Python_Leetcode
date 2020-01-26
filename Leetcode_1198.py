"""
Find Smallest Common Element in All Rows

Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.
If there is no common element, return -1.

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
 

Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in increasing order.
"""

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:                
        # SOLUTION by lee215
        c = collections.Counter()
        
        for row in mat:
            for a in row:
                c[a] += 1
                if c[a] == len(mat):
                    return a
        return -1
        
        # SOLUTION by niosocket
        return min(reduce(lambda x,y: set(x) & set(y), mat), default=-1)
        
        # MY SOLUTION based on lee215 solution
        dic = {}
        
        for row in mat:
            for col in row:
                dic[col] = dic.get(col,0) + 1
                if dic[col] == len(mat):
                    return col
        return -1
