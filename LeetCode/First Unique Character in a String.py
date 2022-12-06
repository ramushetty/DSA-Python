# Input: s = "leetcode"
# Output: 0

# Given a string s, find the first non-repeating character 
# in it and return its index. If it does not exist, return -1.

from typing import List
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 0
        for i in range(len(s)):
            if d[s[i]] == 0:
                return i
        return -1

s = "leetcode"
soluion = Solution()
print(soluion.firstUniqChar(s))