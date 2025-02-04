class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        hmap = {}

        for i in range(m):
            for j in range(n):
                temp = i-j
                if temp in hmap:
                    hmap[temp].append(mat[i][j])
                else:
                    hmap[temp]=[mat[i][j]]
        for item in hmap.items():
            item[1].sort()
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mat[i][j] = hmap[i-j].pop()
        return mat
        