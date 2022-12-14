def firstRepeated(arr, n):
        
        #arr : given array
        #n : size of the array
        d = {}
        min_ind = n + 1
        for i in range(n):
            if arr[i] in d:
                print(d)
                min_ind = min(min_ind,d[arr[i]])
                print(min_ind)
            else:
                d[arr[i]] = i
        if min_ind != n + 1:
            return min_ind
        return -1

arr = [1, 5, 3, 4, 3, 5, 6]
print(firstRepeated(arr,7))