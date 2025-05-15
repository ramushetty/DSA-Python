class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        if n < 3:
            return []
        nums.sort()
        for i in range(n-2):

            if i !=0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            j = i+1
            k = n-1

            while j<k:
                two_sum = nums[j]+nums[k]
                if two_sum > target:
                    k-=1
                elif two_sum < target:
                    j+=1
                else:
                    result.append([nums[k],nums[j],-target])
                    while j<k and nums[j] == nums[j+1]:
                        j+=1
                    while j<k and nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
        return result
        