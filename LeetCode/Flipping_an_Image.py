class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        rows = len(image)
        columns = len(image[0])

        output = [[0]*columns for i in range(rows)]

        for i in range(rows):
            for j in range(columns):
                output[i][j] = image[i][columns-j-1]
        
        for i in range(rows):
            for j in range(columns):
                if output[i][j] == 0:
                    output[i][j] = 1
                else:
                    output[i][j] = 0
        return output