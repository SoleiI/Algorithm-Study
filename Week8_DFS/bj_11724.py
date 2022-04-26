# 백준 11724) 연결 요소
# 입력 : 정점의 개수 N, 간선의 개수 M, 간선의 양 끝점 u, v
# 출력 : 연결 요소의 개수

import sys
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

visit = [0 for _ in range(n)]
def recursive_dfs(v):
  visit[v] = 1
  for w in graph[v]:
    if visit[w] == 0:
      recursive_dfs(w)

count = 0
for i in range(n):
  if visit[i] == 0:
    recursive_dfs(i)
    count += 1

print(count)