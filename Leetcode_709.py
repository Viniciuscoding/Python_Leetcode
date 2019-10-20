"""
To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Example 2:
Input: "here"
Output: "here"

Example 3:
Input: "LOVELY"
Output: "lovely"
"""

class Solution:
    def toLowerCase(self, str: 'str') -> 'str':
    
      # FASTER SOLUTION
      # return str.lower()
      
      # MY SOLUTION
      arr = list(str)
      for i in range(len(arr)):
        decimal = ord(arr[i])
        if decimal >= 65 and decimal <= 90:
            arr[i] = chr(decimal + 32)
        else:
            continue
      return ''.join(arr)

