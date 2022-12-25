def reverse(arr,start,end):

    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1
    return arr


def rotate_an_array(nums,d):

    # l = []
    # for i in range(0,d):
    #     l.append(nums[i])
    # l2 = []

    # for i in range(d,len(num)):
    #     l2.append(nums[i])
    # for i in l:
    #     l2.append(i)
    # return l2
    nums = reverse(nums,0,d-1)
    nums = reverse(nums,d,len(nums)-1)
    nums = reverse(nums,0,len(nums)-1)

    return nums



num = [1,2,3,4,5]
d = 2
print(rotate_an_array(num,d))