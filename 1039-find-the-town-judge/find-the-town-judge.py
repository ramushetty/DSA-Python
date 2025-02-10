class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        COUNT = [0]*(n+1)

        for i in range(len(trust)):
            COUNT[trust[i][0]] = -1
            COUNT[trust[i][1]] +=1
        for i in range(1,len(COUNT)):
            if COUNT[i] == n-1:
                return i
        return -1
        