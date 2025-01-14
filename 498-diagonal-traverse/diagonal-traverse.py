class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        map_diag = {}
        for i in range(m):
            for j in range(n):
                # use i+j technique as it is diagonal travesal 
                if i+j in map_diag:
                    map_diag[i+j].append(mat[i][j])
                else:
                    map_diag[i+j] = [mat[i][j]]
        result = []
        for key in map_diag.items():
            if key[0] % 2 == 0:
                for e in key[1][::-1]:
                    result.append(e)
            else:
                for e in key[1]:
                    result.append(e)
        return result


            
