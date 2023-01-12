class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findFirst(nums,target):
            low = 0 
            high = len(nums) - 1
            index = -1
            while low <= high:

                mid = (low+high) // 2

                if   nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1

                if target == nums[mid]:
                    index = mid
            return index
        def findlast(nums,target):
            low = 0 
            high = len(nums) - 1
            index = -1
            while low <= high:

                mid = (low+high) // 2

                if  nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
                
                if target == nums[mid]:
                    index = mid
            return index
            
        l = [-1,-1]
        l[0] = findFirst(nums,target)
        l[1]  = findlast(nums,target)

        return l

    