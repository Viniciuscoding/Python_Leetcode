"""
Student Attendance Record I

You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""

import re

class Solution:
    def checkRecord(self, s: str) -> bool:
        # MY SOLUTION
        a_count = l_count = 0
    
        for i in range(len(s)):
            if s[i] == 'A':
                a_count += 1
                if a_count > 1:
                    return False
                l_count = 0
            elif s[i] == 'L':
                l_count += 1
                if l_count > 2:
                    return False    
            else:
                l_count = 0
                
        return True
      
        # SOLUTION with .coun() 
        # return s.count('A') < 2 and s.count('LLL') == 0
        
        # SOLUTION by ryan_lv
        # return not re.match(r'.*LLL.*|.*A.*A', s)
        
