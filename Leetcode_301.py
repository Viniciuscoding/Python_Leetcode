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

class Solution(object):
    def removeInvalidParentheses(self, s):
        # SOLUTION by Leetcode
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                else:
                    left -= 1

        def dfs(idx, left, right, left_rem, right_rem, cur):
            if idx == len(s):
                if left_rem == right_rem == 0:
                    self.ans.append(cur)
                    return
            else:
                if s[idx] == "(":
                    if left_rem > 0:
                        dfs(idx + 1, left, right, left_rem - 1, right_rem, cur)
                    dfs(idx + 1, left + 1, right, left_rem, right_rem, cur + "(")
                elif s[idx] == ")":
                    if right_rem > 0:
                        dfs(idx + 1, left, right, left_rem, right_rem - 1, cur)
                    if left > right:  
                        dfs(idx + 1, left, right + 1, left_rem, right_rem, cur + ")")
                else:  
                    dfs(idx + 1, left, right, left_rem, right_rem, cur + s[idx])  # 
        
        self.ans = []
        dfs(0, 0, 0, left, right, "")
        return list(set(self.ans))
