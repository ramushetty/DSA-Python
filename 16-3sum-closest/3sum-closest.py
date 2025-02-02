class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest_sum = 100000
        nums.sort()
        for k in range(0,n-2):

            i = k+1
            j = n-1
            while i < j:
                temp_sum  = nums[i]+nums[j]+nums[k]
                if abs(target - temp_sum) < abs(target-closest_sum):
                    closest_sum = temp_sum
                if temp_sum < target:
                    i+=1
                else:
                    j-=1
        return closest_sum