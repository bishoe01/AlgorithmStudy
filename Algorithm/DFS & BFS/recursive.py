def dfs(graph,v, visited):
    visited[v] = True
    print(v,end="")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

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

visited = [False]*9

dfs(graph,1,visited)