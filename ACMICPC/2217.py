
k = int(input())  # 로프의 개수 입력
limit = []  # 각 로프의 중량한계치 리스트
for i in range(k):
    s = int(input())
    limit.append(s)
limit.sort()  # 순서대로 나열m, 최소중량(answer) = (로프의 개수k) X (로프중 최소한계치) =
min = limit[0]*k
for i in range(1, len(limit)):
    if(min < limit[i]*(k-i)):  # 비교
        min = limit[i]*(k-i)

    # 정답
print(min)
