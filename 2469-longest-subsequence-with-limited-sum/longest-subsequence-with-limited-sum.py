class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        # sort the nums
        nums.sort()
        # take cumulative sum of nums
        for i in range(1,n):
            nums[i] += nums[i-1]
        m = len(queries)
        result = []
        for idx in range(m):
            l = 0
            r = n-1
            res = -1
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] <= queries[idx]:
                    l = mid+1
                    res = mid
                else:
                    r = mid-1
            result.append(res+1)
        return result

        
        