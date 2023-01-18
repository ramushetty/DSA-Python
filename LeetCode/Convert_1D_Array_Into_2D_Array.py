class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        if m*n != l:
            return []
        ans = [[0]*n for _ in range(m)]
        for i in range(l):
            ans[i//n][i%n] = original[i]
        return ans