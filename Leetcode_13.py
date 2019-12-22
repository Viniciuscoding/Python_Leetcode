"""
Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I":  1,
                  "IV": 4,
                  "V":  5,
                  "IX": 9,
                  "X":  10,
                  "XL": 40,
                  "L":  50,
                  "XC": 90,
                  "C":  100,
                  "CD": 400,
                  "D":  500,
                  "CM": 900,
                  "M":  1000}
        
        // MY SOLUTION
        
        integer = 0
        for ro in range(len(s)-1,-1,-1):
            if ro > 0:
                if (s[ro] == "V" or s[ro] == "X") and s[ro - 1] == "I":
                    integer += romans[s[ro]] - 2
                elif (s[ro] == "L" or s[ro] == "C") and s[ro - 1] == "X":
                    integer += romans[s[ro]] - 20
                elif (s[ro] == "D" or s[ro] == "M") and s[ro - 1] == "C":
                    integer += romans[s[ro]] - 200
                else:
                    integer += romans[s[ro]]
            else:
                integer += romans[s[ro]]
            
        return integer
        
        // SOLUTION by 
        res = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
               res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res + roman[s[-1]]
        
        // SOLUTION by 
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
