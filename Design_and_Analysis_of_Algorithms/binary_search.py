def binary_search(array,x):
#array should have been sorted
    left=0
    right=len(array)-1
    while(left<=right):
        middle=int((left+right)/2)
        if x==array[middle]:
            return middle
        if x>array[middle]:
            left=middle+1
        else:
            right=middle-1
    return -1


array=[1,2,5,6,8,10,13,55,100,456,1000]
print(binary_search(array,100))
