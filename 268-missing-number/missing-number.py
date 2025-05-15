class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor1 = 0
        xor2 = 0
        for i in range(0,n):
            xor1 ^= i
            xor2 ^= nums[i]
        xor1 ^= n
        return xor1^xor2
        