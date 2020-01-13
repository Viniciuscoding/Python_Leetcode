"""
Number of Segments in a String

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
Please note that the string does not contain any non-printable characters.

Example: 1 

Input: "Hello, my name is John"
Output: 5
"""

class Solution:
    def countSegments(self, s: str) -> int:
        # MY SOLUTION
        return len(s.split())
        
        # MY OTHER SOLUTION (faster)
        i = 0
        char_arr = []
        while i < len(s):
            if s[i] == " ":
                char_arr.append(0)
                i += 1
            else:
                while s[i] != " ":
                    i += 1
                    if i == len(s):
                        break
                char_arr.append(1)
                    
        return sum(char_arr)
