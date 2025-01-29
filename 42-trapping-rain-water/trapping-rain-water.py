class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # left_max = [0]*n
        # right_max = [0]*n
        # left_max[0] = height[0]
        # right_max[n-1] = height[n-1]
        # max_water = 0

        # for i in range(1,n):
        #     if height[i] > left_max[i-1]:
        #         left_max[i] = height[i]
        #     else:
        #         left_max[i] = left_max[i-1]
        # for i in range(n-2,-1,-1):
        #     if height[i] > right_max[i+1]:
        #         right_max[i] = height[i]
        #     else:
        #         right_max[i] = right_max[i+1]
        # for i in range(n):
        #     temp = min(left_max[i],right_max[i]) - height[i]
        #     max_water += temp
        # return max_water
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n
        trapped_water = 0

        # Fill left_max
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        # Fill right_max
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        # Calculate trapped water
        for i in range(n):
            trapped_water += min(left_max[i], right_max[i]) - height[i]   

        return trapped_water     
        