array = list(map(int,input().split()))

def quick_sort(array,start, end):
    pivot = start
    left = start +1
    right = end
    while(left <= right):
        while(left<= pivot and array[left]<=array[pivot]):
            left+=1
        while(right>pivot and array[right]> array[pivot]):
            right-=1

        if(left>right):
            array[right], array[pivot]  = array[pivot],array[right]
        else:
            array[right], array[left] = array[left], array[right]
    quick_sort(array,start,right-1)
    quick_sort(array,right-1,end)
quick_sort(array,0,len(array)-1)
print(array)