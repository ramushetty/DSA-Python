class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = []
        neg = []
        for ele in nums:
            if ele > 0:
                pos.append(ele)
            else:
                neg.append(ele)
        for i in range(len(pos)):
            nums[2*i] = pos[i]
        for i in range(len(neg)):
            nums[2*i+1] = neg[i]
        return nums
        