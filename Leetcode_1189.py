"""
Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1
Example 2:

Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 
Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
   
      # SOLUTION by cenkay (It is faster than mine)  
      return min(text.count('b'),
                 text.count('a'),
                 text.count('n'),
                 text.count('l')//2,
                 text.count('o')//2)
      
      # MY SOLUTION
      single = "balon"
      count_arr = [0]*(len(single))
        
      for i in range(len(text)):
          if single[0] == text[i]:
              count_arr[0] += 1
          if single[1] == text[i]
              count_arr[1] += 1
          if single[2] == text[i]:
              count_arr[2] += 1
          if single[3] == text[i]:
              count_arr[3] += 1
          if single[4] == text[i]:
              count_arr[4] += 1
        
        # Reduce 'l' and 'o' to half because in a word it requires 2 of each       
        count_arr[2] = count_arr[2] // 2
        count_arr[3] = count_arr[3] // 2
        
        return min(count_arr)
