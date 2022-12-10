
# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

# For each location indices[i], do both of the following:

# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.
# Input: m = 2, n = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.


from typing import List
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:

        # arr = []
        # for i in range(m):
        #     l = []
        #     for j in range(n):
        #         l.append(0)
        #     arr.append(l)
        # for e in indices:
        #     a,b = e[0],e[1]
        #     for i in range(m):
        #         for j in range(n):
        #             if a == i :
        #                 arr[i][j] = arr[i][j] + 1
        #             if b == j:
        #                 arr[i][j] = arr[i][j] + 1

        # for e in indices:
        #     a,b = e[0],e[1]
        #     print(a,b)
        #     for i in range(m):
        #         arr[a][i] += 1
        #     for j in range(n):
        #         print(j)
        #         arr[j][b] += 1
        # count = 0
        # for i in range(m):
        #         for j in range(n):
        #             if arr[i][j] % 2 != 0:
        #                 count += 1
                    
        # return count
        row_data = [0]*m
        col_data = [0]*n
        
        for i,j in indices:
            row_data[i] = row_data[i] + 1
            col_data[j] = col_data[j] + 1
        print(row_data,col_data)
        odd_count = 0 
        for rowp in range(m):
            for colp in range(n):
                val = row_data[rowp] + col_data[colp]
                if val % 2 != 0:
                    odd_count+=1
        
        return odd_count



m = 2
n = 3
indices = [[0,1],[1,1]]
soultion = Solution()
print(soultion.oddCells(m,n,indices))
