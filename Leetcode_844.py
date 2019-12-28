"""
Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

#from functools import reduce

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        # MY SOLUTION
        new_S, new_T = [], []

        for i in range(len(S)):
            if S[i] == "#":
                if len(new_S) == 0:
                    new_S
                else:
                    new_S.pop()
            else:
                new_S.append(S[i])

        for a in range(len(T)):
            if T[a] == "#":
                if len(new_T) == 0:
                    new_T
                else:
                    new_T.pop()
            else:
                new_T.append(T[a])
        
        return new_S == new_T
        
        
        # SOLUTION by lee215
         def backspace(res, char):
             if char != '#':
                 res.append(char)
             elif res:
                 res.pop()
  
             return res
        
         return reduce(backspace, S, []) == reduce(backspace, T, [])


