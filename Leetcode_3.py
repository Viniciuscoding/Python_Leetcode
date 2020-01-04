"""
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    # COULD NOT SOLVE IT
    #def lengthOfLongestSubstring(self, s: str) -> int:
        # set_str = ""
        # for i in s:
        #     if i in set_str:
        #         continue
        #     else:
        #         set_str += i
        # print(set_str)
        # for n in range(len(set_str)):
        #     if set_str[n::] in s:
        #         return len(set_str[n::])
        #     else:
        #         continue
        # return 0 
    
    # SOLUTION by hissho
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            # when char already in dictionary
            if ch in dic:
                # check length from start of string to index
                res = max(res, i-start)
                # update start of string index to the next index
                start = max(start, dic[ch]+1)
            # add/update char to/of dictionary 
            dic[ch] = i
        # answer is either in the begining/middle OR some mid to the end of string
        return max(res, len(s)-start)
