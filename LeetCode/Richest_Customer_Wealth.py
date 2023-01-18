class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # n = len(accounts)

        # max_wealth = 0

        # for b in accounts:
        #     current_sum = sum(b)
        #     max_wealth = max(current_sum,max_wealth)

        # return max_wealth

        return max([sum(i) for i in accounts])