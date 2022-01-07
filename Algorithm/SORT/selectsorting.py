array = list(map(int,input().split()))

for i in range(len(array)):
    bound = i
    for j in range(i+1,len(array)):
        if(array[bound]> array[j]):
            bound = j
        array[i], array[bound] = array[bound],array[i]

print(array)