# 백준 7569) 토마토
# 입력 : 상자의 가로 칸 수 M, 세로 칸 수 N, 상자의 개수 H, 토마토들의 정보
# 출력 : 토마토가 모두 익을 때까지 최소 날짜

import sys
from collections import deque

m, n, h = map(int, input().split())
tomatoes = []
for i in range(h):
  box = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
  tomatoes.append(box)

dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
visited = [[[-1] * m for _ in range(n)] for _ in range(h)]

def bfs(queue, count):
  for q in queue:
    k, i, j = q[0], q[1], q[2]
    tomatoes[k][i][j] = 1
    visited[k][i][j] = 0
  while queue:
    v = queue.popleft()
    count += 1
    for d in range(6):
      z = v[0] + dz[d]
      x = v[1] + dx[d]
      y = v[2] + dy[d]
      if 0 <= x < n and 0 <= y < m and 0 <= z < h and tomatoes[z][x][y] == 0:
        queue.append([z, x, y])
        tomatoes[z][x][y] = 1
        visited[z][x][y] = 1 + visited[v[0]][v[1]][v[2]]
  if count == m * n * h:
    return visited[v[0]][v[1]][v[2]]
  else:
    return -1

queue = deque()
count = 0
for k in range(h):
  for i in range(n):
    for j in range(m):
      if tomatoes[k][i][j] == 1:
        queue.append([k, i, j])
      elif tomatoes[k][i][j] == -1:
        count += 1

print(bfs(queue, count))