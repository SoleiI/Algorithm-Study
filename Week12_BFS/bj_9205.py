# 백준 9025) 맥주 마시면서 걸어가기
# 입력: 테스트케이스 개수 t, 편의점 개수 n, 집, 편의점, 락 페스티벌 좌표
# 출력: happy 또는 sad

import sys
from collections import deque
t = int(sys.stdin.readline())

def bfs(start_v):
  visited[start_v] = 1
  queue = deque([start_v])
  while queue:
    v = queue.popleft()
    vv = coordinates[v]
    for w in range(len(graph[v])):
      if visited[w] == 0:
        ww = coordinates[w]
        if abs(ww[0] - vv[0]) + abs(ww[1] - vv[1]) > 1000:
          continue
        queue.append(w)
        visited[w] = 1
  if visited[-1] == 0:
    print('sad')
  else:
    print('happy')

while t > 0:
  n = int(sys.stdin.readline())
  graph = [[] for _ in range(n+2)]
  coordinates = []
  for i in range(n+2):
    a, b = map(int, sys.stdin.readline().split())
    for j in range(n+2):
      if i == j :
        coordinates.append([a, b])
      graph[j].append([a, b])

  visited = [0] * (n+2)
  
  bfs(0)

  t -= 1