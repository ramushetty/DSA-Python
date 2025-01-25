class Solution:
    def overlapcount(self,img1,img2,row_offset,col_offset):
        n = len(img1)
        count = 0
        for i in range(n):
            for j in range(n):
                img2_i = i+row_offset
                img2_j = j + col_offset
                if img2_i < 0 or img2_j<0 or img2_i >=n or img2_j >= n:
                    continue
                if img1[i][j] == 1 and img2[img2_i][img2_j] == 1:
                    count += 1

        return count
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        matrix_length = len(img1)
        max_overlap_count = 0
        for row_offset in range(-matrix_length+1,matrix_length,1):
            for col_offset in range(-matrix_length+1,matrix_length,1):
                temp_count = self.overlapcount(img1,img2,row_offset,col_offset)
                max_overlap_count = max(temp_count,max_overlap_count)
        return max_overlap_count
        