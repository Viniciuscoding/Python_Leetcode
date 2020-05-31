"""
Sparse Matrix Multiplication

Given two sparse matrices A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

class Solution(object):
    def multiply(self, A, B):
        m = len(A)
        n = len(A[0])
        k = len(B[0])
        AB = [[0 for _ in range(k)] for _ in range(m)]
        
        # Pick up each row
        for i, rowA in enumerate(A):

             # Pick up each element of the row
            for K, elA in enumerate(rowA):
                # If the element is zero than ignore the calculation else calculate
                if elA != 0:
                    colB = B[K] # I am adding this variable for easier understanding
                    for j, elB in enumerate(colB): # This is the column of B matrix
                        if elB != 0:
                            # Multiply each element and add them in their respective position
                            AB[i][j] += elA * elB
        return AB
