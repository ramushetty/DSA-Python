# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        # s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL','XXXX').replace('XC', 'LXXXX').replace('CD','CCCC').replace('CM','DCCCC')

        # num = 0
        # for c in s:
        #     num += roman_to_integer[c]
        # return num
        num = 0
        for c in range(len(s)-1):
            if roman_to_integer[s[c]] < roman_to_integer[s[c+1]]:
                num -= roman_to_integer[s[c]]
            else:
                num += roman_to_integer[s[c]]
        return num+roman_to_integer[s[-1]]
inp = "MCMXCIV"
soluion = Solution()
print(soluion.romanToInt(inp))



