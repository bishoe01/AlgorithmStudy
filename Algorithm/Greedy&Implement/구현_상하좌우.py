


N =  int(input())
plan = [k for k in input().split()] ## 움직일 계획 L U R D 로 명령을 리스트형태로 내릴 것 
# for i in range(N):   #지도의 크기 N*N형태의 정사각형 지도 
#     for k in range(N):
#         print(f"({i+1}, {k+1})",end=" ")
#     print()



x , y = 1, 1
for move in plan:
    if(y==1 and move=='L'):
        pass
        print(x,y)
    if(x==1 and move=='U'):
        pass
        print(x, y)
    elif(move=='L'):
        y -= 1
        print(x, y)
    elif ( move == 'U'):
        x -= 1
        print(x, y)
    elif (move == 'D'):
        x += 1
        print(x, y)
    elif (move == 'R'):
        y += 1
        print(x, y)
print(f"목적지 도착 : {x,y}")
