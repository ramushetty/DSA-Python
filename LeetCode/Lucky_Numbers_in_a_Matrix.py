class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        min_row  = [min(x) for x in matrix]
        max_col = [max(x) for x in zip(*matrix)]

        m = len(matrix)
        n = len(matrix[0])
        res = []
        for i in range(m):
            for j in range(n):

                if min_row[i] == max_col[j]:
                    res.append(min_row[i])
        return res