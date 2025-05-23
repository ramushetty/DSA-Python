class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        result = []
        nums.sort()
        for i in range(n-3):
            if i !=0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                k = j+1
                l = n-1

                while k<l:
                    sum_ = nums[i]+nums[j]+nums[k]+nums[l]
                    if sum_ == target:
                        result.append([nums[i],nums[j],nums[k],nums[l]])
                        while k < l and nums[k] == nums[k+1]:
                            k+=1
                        while k<l and nums[l] == nums[l-1]:
                            l-=1
                        k+=1
                        l-=1
                    elif sum_< target:
                        k+=1
                    else:
                        l-=1
        return result


        