class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for w in words:
            for c in w:
                if c not in allowed:
                    count += 1
                    break
        return len(words) - count
                