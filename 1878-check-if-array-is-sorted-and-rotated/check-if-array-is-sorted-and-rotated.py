class Solution:
    def check(self, nums: List[int]) -> bool:

        check = 1 
        n = len(nums)
        for i in range(1,2*n):
            if nums[(i-1)%n] <= nums[i%n]:
                check+=1
            else:
                check = 1
            if check == n:
                return True
        return n == 1
        