
from collections import deque  #큐 생성

def bfs(graph,start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True



graph = [  #인접한 노드들을 2차원 배열로 표현
    [],  #인덱스 0 은 지워두기
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]* 9
bfs(graph,1,visited)
