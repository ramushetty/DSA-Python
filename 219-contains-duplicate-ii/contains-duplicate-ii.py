class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp = {}
        for index in range(len(nums)):
            if nums[index] in mapp and (abs(mapp[nums[index]] - index) <= k):
                return True
            else:
                mapp[nums[index]] = index
        return False
        