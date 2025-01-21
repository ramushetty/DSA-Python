class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = {}
        hmap[0] = -1
        sub_array_sum = 0
        for index in range(len(nums)):
            sub_array_sum += nums[index]
            remainder = sub_array_sum%k
            if remainder in hmap:
                if(index - hmap[remainder]) >= 2:
                    return True
            else:
                hmap[remainder] = index
        return False
        