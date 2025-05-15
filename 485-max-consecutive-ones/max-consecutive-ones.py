class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0
        for ele in nums:
            if ele == 1:
                count +=1
                if count > maxi:
                    maxi = count
            else:
                count = 0
        return maxi
            
        