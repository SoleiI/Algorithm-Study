# 백준 1520) 내리막 길
# 입력 : 세로 크기 M, 가로 크기 N, 각 지역의 높이 정보
# 출력 : 이동 가능한 경로의 수

import sys
sys.setrecursionlimit(10**7)
m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(i, j, visit):
  global count
  visit.append([i, j])
  for c in range(4):
    x = i + dx[c]
    y = j + dy[c]
    if 0 <= x < m and 0 <= y < n:
      if [x, y] in visit:
        continue
      if graph[x][y] < graph[i][j]:
        if x == m-1 and y == n-1:
          count += 1
        dfs(x, y, visit)
  visit.pop()

count = 0
dfs(0, 0, [])
print(count)