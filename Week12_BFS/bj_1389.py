# 백준 1389) 케빈 베이컨의 6단계 법칙
# 입력 : 유저의 수 N, 친구 관계의 수 M, 친구 관계 정보
# 출력 : 케빈 베이컨의 수가 가장 작은 사람

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(start_v):
  visited[start_v] = 0
  queue = deque([start_v])
  while queue:
    v = queue.popleft()
    for w in graph[v]:
      if visited[w] == -1:
        queue.append(w)
        visited[w] = visited[v] + 1

minDegree = (0, 1000)

for i in range(1, n+1):
  visited = [-1] * (n+1)
  bfs(i)
  kbDegree = (i, sum(visited))
  minDegree = kbDegree if kbDegree[1] < minDegree[1] else minDegree

print(minDegree[0])