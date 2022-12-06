# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        newNum = 0
        while x > 0:
            newNum = newNum *10 + x % 10
            x = x // 10
        return temp == newNum

x = 121
soultion = Solution()
print(soultion.isPalindrome(x))   