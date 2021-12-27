#K번째 수 문제풀이
def solution(array, commands):
    answer = []  ##정답 리스트 초기화
    for x in commands:
        tmpx = x[0]-1 #commands 배열의 원소마다의 길이가 3이므로 index값 0,1일때는 항상 i ,j 값이다 
        tmpy = x[1]
        target = x[2]-1   # -1하는이유는 문제에서는 인덱스 값이 아닌 ?번째 수를 구하라했으니 인덱스값에서 -1을 해줬음
        C = (array[tmpx:tmpy])  #슬라이스 해주면 된다)
        C.sort()  #정렬해주기 
        answer.append(C[target])  #정답 리스트에 원소 추가해주기

    return answer
