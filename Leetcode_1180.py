"""
Count Substrings with Only One Distinct Letter

Given a string S, return the number of substrings that have only one distinct letter.

Example 1:

Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.

Example 2:

Input: S = "aaaaaaaaaa"
Output: 55
 

Constraints:

1 <= S.length <= 1000
S[i] consists of only lowercase English letters.
"""

class Solution:
    def countLetters(self, S: str) -> int:
        # MY SOLUTION
        arr_per = []
        total = 0
        count = 1
        ind = 0
        S = S + 'A'
        
        while ind < len(S) - 1:
            if S[ind] == S[ind + 1]:
                count += 1
                ind += 1
            else:
                arr_per.append(count)
                count = 1
                ind += 1
                if ind == (len(S) - 1):
                    arr_per.append(count)
        loop = 0
        for i in arr_per:
            loop = i
            while loop != 0:
                total += loop
                loop -= 1        
        
        return total - 1  
