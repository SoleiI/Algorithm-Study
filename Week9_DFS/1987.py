# 백준 1987) 알파벳
# 입력 : R, C, 알파벳
# 출력 : 말이 지날 수 있는 최대의 칸 수

import sys
sys.setrecursionlimit(10**7)
r, c = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline().rstrip() for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visit = [[False] * c for _ in range(r)]
alpha = [False] * 26
maxAlpha = 0
def recursive_dfs(i, j, alphabets):
  global maxAlpha
  visit[i][j] = True
  alpha[ord(graph[i][j])-65] = True
  alphabets.append(graph[i][j])
  for n in range(4):
    x = i + dx[n]
    y = j + dy[n]
    if 0 <= x < r and 0 <= y < c:
      if visit[x][y]:
        visit[x][y] = False
        continue
      if alpha[ord(graph[x][y])-65]:
        alpha[ord(graph[x][y])-65] = False
        continue
      else:
        recursive_dfs(x, y, alphabets)
        maxAlpha = len(alphabets) if len(alphabets) > maxAlpha else maxAlpha
        alphabets.pop()
        visit[i][j] = False
        alpha[ord(graph[i][j])-65] = False
  return alphabets

recursive_dfs(0, 0, [])
print(maxAlpha)