class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_ind = self.min_ind(nums)
        f = self.bs(nums,target,0,min_ind-1)
        s = self.bs(nums,target,min_ind,len(nums)-1)

        if f != -1:
            return f
        if s != -1:
            return s
        return -1 


    def bs(self,arr,target,start,end):

        while start <= end:
            mid = start + (end-start)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid+1
            else:

                end = mid -1
        return -1
    def min_ind(self,arr):
        start = 0
        end = len(arr) -1
        n = len(arr)
        if n == 1:
            return 0
        
        if arr[end] > arr[0]:
            return 0
        
        while start <= end:
            mid = start + (end-start)//2
            if arr[mid] > arr[mid+1]:
                return mid+1
            if arr[mid-1] > arr[mid]:
                return mid
            if arr[mid] > arr[0]:
                start = mid + 1
            else:
                end = mid -1 