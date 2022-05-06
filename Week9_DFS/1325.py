# 백준 1325) 효율적인 해킹
# 입력 : N, M, 신뢰 관계
# 출력 : 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호 오름차순

import sys
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
graph = {}

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  if b not in graph:
    graph[b] = {a}
  else:
    graph[b].add(a)

def recursive_dfs(v):
  global count
  visit[v] = 1
  if v in graph:
    for w in graph[v]:
      if visit[w] == 0:
        count += 1
        recursive_dfs(w)

computers = [0] * (n + 1)
for i in range(1, n+1):
  visit = [0] * (n + 1)
  count = 0
  recursive_dfs(i)
  computers[i] = count

for i in range(len(computers)):
  if max(computers) == 0:
    print(0)
    break
  if computers[i] == max(computers):
    print(i, end=" ")
