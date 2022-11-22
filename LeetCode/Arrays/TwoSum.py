# method-1 brute force
from typing import List


class Solution:
    def twoSumButeForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            temp = nums[i]
            for j in range(i+1,len(nums)):
                if temp + nums[j] == target:
                    return [i,j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i,hashmap[complement]]  
            hashmap[nums[i]] = i
            
solution  = Solution()
nums = [2,7,11,15]
target = 9
print(solution.twoSumButeForce(nums,target))
print(solution.twoSum(nums,target))

