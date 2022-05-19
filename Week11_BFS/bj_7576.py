# 백준 7576) 토마토
# 입력 : 상자의 가로 칸 수 M, 세로 칸 수 N, 토마토들의 정보
# 출력 : 토마토가 모두 익을 때까지 최소 날짜

import sys
from collections import deque

m, n = map(int, input().split())
tomatoes = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[-1] * m for _ in range(n)]

def bfs(queue, count):
  for q in queue:
    i, j = q[0], q[1]
    tomatoes[i][j] = 1
    visited[i][j] = 0
  while queue:
    v = queue.popleft()
    count += 1
    for d in range(4):
      x = v[0] + dx[d]
      y = v[1] + dy[d]
      if 0 <= x < n and 0 <= y < m and tomatoes[x][y] == 0:
        queue.append([x, y])
        tomatoes[x][y] = 1
        visited[x][y] = 1 + visited[v[0]][v[1]]
  if count == m * n:
    return visited[v[0]][v[1]]
  else:
    return -1

queue = deque()
count = 0
for i in range(n):
  for j in range(m):
    if tomatoes[i][j] == 1:
      queue.append([i, j])
    elif tomatoes[i][j] == -1:
      count += 1

print(bfs(queue, count))