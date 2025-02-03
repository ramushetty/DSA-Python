class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        right = n-1
        down = m-1
        left = 0
        result = []
        d = 0
        while top <= down and left <= right:
            if d == 0:
                for i in range(left,right+1):
                    result.append(matrix[top][i])
                top+=1
            if d == 1:
                for i in range(top,down+1):
                    result.append(matrix[i][right])
                right -= 1
            if d==2:
                for i in range(right,left-1,-1):
                    result.append(matrix[down][i])
                down -=1
            if d==3:
                for i in range(down,top-1,-1):
                    result.append(matrix[i][left])
                left +=1
            d +=1
            if d ==4:
                d=0
        return result


        