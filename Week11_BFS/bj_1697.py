# 백준 1697) 숨바꼭질
# 입력 : 수빈이의 위치 N, 동생의 위치 K
# 출력 : 수빈이가 동생을 찾는 가장 빠른 시간

import sys
n, k = map(int, sys.stdin.readline().split())

def bfs(start_v):
  visited = [-1] * 100001
  queue = [start_v]
  visited[start_v] = 0
  while queue:
    v = queue.pop(0)
    if v == k:
      return visited[v]
    for w in [v+1, v-1, v*2]:
      if w < 0 or w > 100000:
        continue
      if visited[w] == -1:
        queue.append(w)
        visited[w] = 1 + visited[v]
        if w == k:
          return visited[w]

print(bfs(n))