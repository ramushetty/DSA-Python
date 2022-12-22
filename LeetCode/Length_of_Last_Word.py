class Solution:
    def lengthOfLastWord(self, s: str) -> int:
            # s = s.strip()
            ss = s.split()[-1]
            return len(ss)