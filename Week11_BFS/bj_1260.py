# 백준 1260) DFS와 BFS
# 입력 : 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V, 간선 정보
# 출력 : DFS 수행 결과, BFS 수행 결과

import sys
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for g in graph:
  g.sort()

def dfs(v, visited):
  visited.append(v)
  for w in graph[v]:
    if w not in visited:
      dfs(w, visited)
  return visited

def bfs(start_v):
  visited = [start_v]
  queue = [start_v]
  while queue:
    v = queue.pop(0)
    for w in graph[v]:
      if w not in visited:
        visited.append(w)
        queue.append(w)
  return visited

dfs_list = dfs(v, [])
bfs_list = bfs(v)

print(*dfs_list, sep=' ')
print(*bfs_list, sep=' ')
