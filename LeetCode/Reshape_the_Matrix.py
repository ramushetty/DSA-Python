class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat[0])
        n = len(mat)

        if r*c != m*n:
            return mat
        else:
            new_mat = [[0]*c for _ in range(r)]
            for i in range(r*c):
                new_mat[i//c][i%c] = mat[i//m][i%m]
            return new_mat
