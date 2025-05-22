class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        st = set()
        for ele in nums:
            st.add(ele)
        
        longest = 1
        for ele in st:
            if ele-1 not in st:
                cnt = 1
                x = ele
                while x+1 in st:
                    x += 1
                    cnt +=1
                longest = max(longest,cnt)
        return longest
        