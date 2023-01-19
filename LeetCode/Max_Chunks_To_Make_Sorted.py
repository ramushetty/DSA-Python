class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max = 0
        chunks = 0
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
            if max == i:
                chunks += 1
        return chunks