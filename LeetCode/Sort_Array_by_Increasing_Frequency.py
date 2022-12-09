# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
# If multiple values have the same frequency, sort them in decreasing order.

# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
from collections import Counter
from typing import List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:  

        c = Counter(nums)
        r = c.most_common()

        r.sort(key=lambda x : x[0], reverse=True)
        r.sort(key= lambda x : x[1])

        t = []
        print(r)
        for i in r:
            a,b = i
            t.extend([a]*b)

        return t




nums = [1,1,2,2,2,3]
solution = Solution()
print(solution.frequencySort(nums))