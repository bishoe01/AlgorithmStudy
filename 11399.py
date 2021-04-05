# 백준#11399번 그리디 알고리즘 python 풀이

n = int(input())  # 대기 인원 수
c = [int(x) for x in input().split()]  # 사람마다 걸리는 시간 입력받기

c.sort()  # 오래안걸리는 사람부터로 정렬 (최솟값 구하기)
sum = 0     # 손님당 기다리는 시간
time = 0    # 전체 소요시간

for i in range(0, len(c)):
    sum += c[i]
    time += sum
print(time)
