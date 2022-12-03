# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3


from typing import List

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        for i in stones:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        count = 0

        for i in jewels:
            if i in d:
                count += d[i]
        return count


        
jewels = "aA"
stones = "aAAbbbb"
soluion = Solution()
print(soluion.numJewelsInStones(jewels,stones))

