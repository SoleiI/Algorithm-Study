# 백준 1325) 효율적인 해킹
# 입력 : N, M, 신뢰 관계
# 출력 : 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호 오름차순

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[b].append(a)

def bfs(start_v):
  visited = [0] * (n+1)
  queue = deque([start_v])
  visited[start_v] = 1
  count = 0
  while queue:
    v = queue.popleft()
    for w in graph[v]:
      if visited[w] == 0:
        queue.append(w)
        visited[w] = 1
        count += 1
  return count

maxComputers = []
max = 0
for i in range(1, n+1):
  computers = bfs(i)
  if max > computers:
    continue
  elif max == computers:
    maxComputers.append(i)
  else:
    max = computers
    maxComputers = []
    maxComputers.append(i)

print(*maxComputers)