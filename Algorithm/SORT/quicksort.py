array = list(map(int,input().split()))

def quicksort(array,start,end):
    pivot = start
    left = start+1
    right = end

    while(left<=right):
        while(left<=pivot and array[left]<=array[pivot]):
            left+=1
        while(right>pivot and array[right]> array[pivot]):
            right-=1
        if(left>right):
            array[right],array[pivot] = array[pivot],array[left]
        else:
            array[right],array[left] = array[left],array[right]
    quicksort(array,0,right-1)
    quicksort(array, right - 1,end)
quicksort(array,0,len(array)-1)
print(array)