# using Temporary array

#using two pointer approach
arr = [1,2,3,4,5]

low = 0
high = len(arr)-1

while(low < high):
    # swap
    temp = arr[low]
    arr[low] = arr[high]
    arr[high] = temp
    low += 1
    high -= 1

print(arr)



lst = [10, 11, 12, 13, 14, 15]
lst.reverse()     # in place
print("Using reverse() ", lst)
 
print("Using reversed() ", list(reversed(lst)))


# using slicing memory will be exusted if array size is big
new_lst = lst[::-1]