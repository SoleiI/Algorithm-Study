# 백준 5014) 스타트링크
# 입력 : F, S, G, U, D (건물 층 정보)
# 출력 : S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값 또는 use the stairs

import sys
from collections import deque
f, s, g, u, d = map(int, sys.stdin.readline().split())
visited = [-1] * (f+1)

def bfs(s, g):
  visited[s] = 0
  queue = deque([s])
  if s == g:
    return 0
  elif s < g and u == 0:
    return -1
  elif s > g and d == 0:
    return -1
  while queue:
    v = queue.popleft()
    for w in [v+u, v-d]:
      if w > f or w < 1:
        continue
      if visited[w] == -1:
        queue.append(w)
        visited[w] = visited[v] + 1
        if w == g:
          return visited[w]
  return visited[g]

floors = bfs(s, g)
if floors == -1:
  print('use the stairs')
else:
  print(floors)
