class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumEven = 0
        for e in nums:
            if e%2 == 0:
                sumEven+=e
        result = []

        queries_len = len(queries)

        for query in queries:
            val = query[0]
            indx = query[1]

            if nums[indx] %2 ==0:
                sumEven -= nums[indx]

            nums[indx] += val

            if nums[indx] % 2 == 0:
                sumEven += nums[indx]

            result.append(sumEven)
        return result       