# 백준 2573) 빙산
# 입력: 행의 개수 N, 열의 개수 M, 각 칸의 정보
# 출력: 빙산이 분리되는 최초의 시간(년)

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(start, count):
  visited[start[0]][start[1]] = True
  queue = deque([start])
  while queue:
    v = queue.popleft()
    water = 0
    for d in range(4):
      x = v[0] + dx[d]
      y = v[1] + dy[d]
      if 0 <= x < n and 0 <= y < m:
        if iceberg[x][y] <= 0:
          visited[x][y] = True
          water += 1
        elif visited[x][y] == False:
          queue.append([x, y])
          visited[x][y] = True
    melted[v[0]][v[1]] = iceberg[v[0]][v[1]] - water
  count += 1
  return count

year = 0

while True:
  count = 0
  zero = 0
  visited = [[False] * m for _ in range(n)]
  melted = [[0] * m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if iceberg[i][j] <= 0:
        zero += 1
        continue
      elif visited[i][j]:
        continue
      else:
        count = bfs([i, j], count)
  if count > 1:
    print(year)
    break
  if zero == n*m:
    print(0)
    break
  year += 1
  iceberg = list(melted)