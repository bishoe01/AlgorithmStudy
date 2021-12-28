## N값이 주어지며 00사00분00초부터 N시간까지 도달하는 중에 3이 들어가는 횟수를 카운트하라

N = int(input())

count3 = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):  #N시간까지 60분 60초 이기때문에 3차원배열형성
            if('3' in str(h)+str(m)+str(s)): ##3이라는 숫자를 문자열로 바꿔준뒤 카운팅한다
                count3+=1

print(count3)
