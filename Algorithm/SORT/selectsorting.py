array = list(map(int,input().split()))

for i in range(len(array)):
    bound_index = i
    for j in range(i+1,len(array)):
        if(array[bound_index]> array[j]):
            bound_index = j
    array[bound_index], array[i] =  array[i],array[bound_index]
print(array)