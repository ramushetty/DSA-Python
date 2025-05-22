class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
         
        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = col-1
        top = 0
        bottom = row-1
        d =1
        ans = []
        while left <= right and top <= bottom:
            if d == 1:
                for i in range(left,right+1):
                    ans.append(matrix[top][i])
                top+=1
            if d == 2:
                for i in range(top,bottom+1):
                    ans.append(matrix[i][right])
                right -=1
            if d ==3:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1
            if d ==4:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
            d +=1
            if d ==5:
                d=0
        return ans
