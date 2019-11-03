"""
Complex Number Multiplication

Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:
The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. 
And the output should be also in this form.
"""

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        # SOLUTION BY zfqan
        a, ai = map(int, a[:-1].split("+"))
        b, bi = map(int, b[:-1].split("+"))
        
        # Equation
        # a*b + i(a*bi) + i(b*ai) + i^2(ai*bi) = a*b + i(a*bi + b*ai) + i^2(ai*bi) = a*b - ai*bi + i(a*b + b*a)
        
        # i^2(ai*bi) will always be - due to i^2 -> -1(ai*bi)
        # first number is always the inverse multiplication of its extremes such as x^2 - y^2
        x2_y2 = a*b - ai*bi
        # a*bi + b*ai will always + each other such as 2xy or xy + xy
        _2xy = a*bi + b*ai

        return "{}+{}i".format(x2_y2, _2xy)
