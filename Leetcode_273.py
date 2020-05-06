"""
Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"

Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

class Solution(object):
    def numberToWords(self, num):
        oneto19 = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        
        def n2words(n):
            if n < 20:
                return oneto19[n-1:n]
            if n < 100:
                return [tens[n/10-2]] + n2words(n%10)
            if n < 1000:
                return [oneto19[n/100-1]] + ["Hundred"] + n2words(n%100)
            if n < 1000000:
                return n2words(n / 1000) + ["Thousand"] + n2words(n % 1000)
            if n < 1000000000:
                return n2words(n / 1000000) + ["Million"] + n2words(n % 1000000)
            if n < 2**31:
                return n2words(n / 1000000000) + ["Billion"] + n2words(n % 1000000000)
        return " ".join(n2words(num)) or "Zero"
        
# EXPLANATION

# 1. Create arrays of specific number names: 1 to 19 and 20,30,...,90
# 2. Build a recursive solution where you check for the following order:
#     2.1 Check for numbers < 19
#     2.2 Check for numbers < 100
#     2.3 Check for numbers < 1000 Notice that any number >= 100 and < 1000 you add the name hundred and check for step 2.2 or 2.1 again.
#     2.4 The pattern of 2.3 happens to Thousands, Millions and Billions decimal cases, so we can write the following pattern.
#     2.5 Check for the highest case value so you can concatanate the case name to it then you concatane the remaning of that
#         value.
# 3. This pattern will concur until it gets to its smallest case.
# 4. Join all the arrays separated by a space in order to return a single string.
