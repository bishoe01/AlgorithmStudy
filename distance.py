# 가까운 매장 좌표를 튜플리스트 형태로 출력하기

# 제곱근 사용을 위한 sqrt 함수
from math import sqrt
import math
# 두 매장의 직선 거리를 계산해 주는 함수


def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수


def closest_pair(coordinates):
    d = []
    d.append(coordinates[0])
    d.append(coordinates[1])
    tmp = distance(coordinates[0], coordinates[1])
    for i in range(len(coordinates)-2):
        for x in range(i+1, len(coordinates)-1):
            if(tmp >= distance(coordinates[i], coordinates[x+1])):
                tmp = distance(coordinates[i], coordinates[x+1])
                del d[0]
                del d[0]
                d.append(coordinates[i])
                d.append(coordinates[x+1])

    return [d[0], d[1]]


    # 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
