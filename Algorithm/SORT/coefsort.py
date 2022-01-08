array = list(map(int,input().split()))

tmp = [0]*(max(array)+1)

for i in range(len(array)):
    tmp[array[i]] +=1

for i in range(len(tmp)):
    for j in range(tmp[i]):
        print(i, end=' ')

