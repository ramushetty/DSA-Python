class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mp = {}
        for element in nums:
            mp[element] = mp.get(element,0) + 1
        duplicate = 0
        for key,value in mp.items():
            if value == 2:
                duplicate = key
                break
        missing  = 0
        for index in range(1,len(nums)+1):
            if index not in nums:
                missing  = index
                break
        return [duplicate,missing]
        