"""
Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 
Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        opened, closed = [], []
        
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                opened.append(i)
            elif char == ')':
                if len(opened) == 0:
                    closed.append(i)
                else:
                    opened.pop()

        openclosedleftover = set(opened + closed)

        return ''.join(s[j] for j in range(len(s)) if j not in openclosedleftover)
    
    
    # EXPLANATION
    
    # Loop through in order to find each parentheses sign ( and ).
    # Every time ech sign is found store them on their respective array, opened or closed array.
    # Check if ( match ) while looping through the word. If a match happens with closed ')' then
    # remove the index from array opened.
    # Concatenate opened and closed array and sort it to make sure it is in the correct order of 
    # indexes since closed array might have early indexes values in closed array.
