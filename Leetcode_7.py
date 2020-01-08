"""
Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note: Assume we are dealing with an environment which could only store integers within the 32-bit signed 
integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when
the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        swp_str = ""
        swp_int = 0
        
        if x_str[0] == '-':
            swp_str = x_str[1::][::-1]
        else:
            swp_str = x_str[::-1]
        
        swp_int = int(swp_str)
        
        if swp_int > 2**31 - 1:
            return 0
        if swp_int < -(2**31):
            return 0
        
        if x_str[0] == '-':
            return -swp_int
        else:
            return swp_int
