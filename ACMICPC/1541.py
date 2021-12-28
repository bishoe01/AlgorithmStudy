modify = input().split('-')  # 입력받은 수식에서 -를 기준으로 나눠줍니다 (최솟값구하기)
main = []      # -를 기준으로 수식덩어리들을 리스트에 넣어줍니다
for i in modify:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)  # 수식들중에 +부호로 묶여있는 수식들을 더해줍니다.
    main.append(sum)  # 정리된 형태로 리스트에 넣어줍니다,

answer = main[0]
for i in range(1, len(main)):
    answer -= main[i]
print(answer)
