"""
ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # I found the algorithm pattern. I could not figure out the algorithm formula
        # PAYPALISHIRING
        # 01210121012101 I need to create a loop that create this number pattern
        #                and store the characters in an array with the number of rows.
        
        # SOLUTION by pharrellyhy
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an empty string array with the number of rows
        zigzag = [''] * numRows  # ['', '', '']
        
        index = move = 0
        
        # Algorithm formula from pharrellyhy
        for char in s:
            # concatenate strings within an array cells
            zigzag[index] += char
            # if index is 0 then you move upwards by 1
            if index == 0:
                move = 1
            # if index is less then numRows you move downwards by 1
            elif index == numRows -1:
                move = -1
            # increment or decrement the index based on move direction
            index += move
        
        return ''.join(zigzag)
