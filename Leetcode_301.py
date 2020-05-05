"""
Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]

xample 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:

Input: ")("
Output: [""]
"""

class Solution(object):
    def removeInvalidParentheses(self, s):

        def validation(s):
            count = 0

            for p in s:
                if p == '(':
                    count += 1
                elif p == ')':
                    count -= 1
                    if count < 0:
                        return False

            return count == 0
        
        posblits = {s}
        
        while True:
            valid = filter(validation, posblits)
            print(valid)
            if valid:
                return valid
            posblits = {s[:i] + s[i+1:] for s in posblits for i in range(len(s))}
            print(posblits)
            
# EXPLANATION

# 1. I brute forced it.
# 2. I removed one parentheses at a time and checked if new word without this parentheses was valid as a sequence of
#    parentheses within words.
# 3. Returned unique sequences as result in an array format.
