    # ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
    # [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
    # Output
    # [null, 8, null, 2, 1, null, null, 11]

# Add a positive integer to an element of a given index in the array nums2.
# Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value
#  (0 <= i < nums1.length and 0 <= j < nums2.length).

from typing import List
from collections import defaultdict
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = {}
        for x in nums2: 
            if x in self.freq:
                self.freq[x] += 1
            else:
                self.freq[x] = 1

    def add(self, index: int, val: int) -> None:
        self.freq[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1

        

    def count(self, tot: int) -> int:
        ans = 0 
        for x in self.nums1: 
            ans += self.freq[tot - x]
        return ans 



fsp = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
print(fsp.count(7))
print(fsp.add(3,2))
# inp1 = ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
# inp2 = [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]

