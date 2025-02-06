class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])

        count = 1
        prev = points[0]
        n = len(points)
        for i in range(1,n):
            prevSP = prev[0]
            prevEP = prev[1]
            currSP = points[i][0]
            currEP = points[i][1]
            if currSP > prevEP:
                count+=1
                prev = points[i]
            else:
                prev[0] = max(currSP,prevSP)
                prev[1] = min(currEP,prevEP)

        return count
        
        