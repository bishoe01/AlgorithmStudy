N, K = map(int, input().split())
variable = [int(input()) for _ in range(N)]

ccount = 0  # 동전 카운팅
while(K != 0):
    for i in range(len(variable)-1, -1, -1):
        if(K > variable[i]):
            ccount += K//variable[i]
            K = K % variable[i]
print(ccount)
