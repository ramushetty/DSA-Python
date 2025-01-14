class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        result = []
        if nums_len < 3:
            return []

        # n1 + n2 + n3 = 0
        # n1 + n2 = -n3 both are same
        
        nums.sort() # sort the nums

        # fix one element n1
        for i in range(0, nums_len-2):
            # remove duplicate
            if i !=0 and nums[i] == nums[i-1]:
                continue
            
            self.twoSum(nums, -nums[i], result, i+1)
        return result
    def twoSum(self,nums,target,result, start_index):

        i = start_index
        j = len(nums)-1
        while i < j:
            elements_sum = nums[i] + nums[j]
            if elements_sum > target:
                j -=1
            elif elements_sum < target:
                i +=1
            else:
                result.append([-target,nums[i],nums[j]])
                while i<j and nums[i] == nums[i+1]: i+=1
                while i<j and nums[j] == nums[j-1]: j-=1
                i+=1
                j-=1


        