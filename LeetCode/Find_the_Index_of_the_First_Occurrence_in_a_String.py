"""
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""

from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        h = len(haystack)
        n = len(needle)

        for i in range(h-n+1):

            k = 0

            for j in range(n):

                if needle[j] != haystack[i+j]:
                    break

                k +=1
            if k == n:
                return i
        return -1        



haystack = "aaa"
needle = "aaaa"
solution = Solution()
print(solution.strStr(haystack,needle))

