# 백준 13023) ABCDE
# 입력 : 사람의 수 N, 관계의 수 M, 관계 정보
# 출력 : 조건에 맞는 A, B, C, D, E 존재 여부

import sys
sys.setrecursionlimit(10**7)
n, m = map(int, sys.stdin.readline().split())
friends = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  friends[a].append(b)
  friends[b].append(a)

def dfs(v, depth):
  global maxDepth
  visit[v] = True
  for w in friends[v]:
    if visit[w] == False:
      dfs(w, depth+1)
    else:
      maxDepth = depth if depth > maxDepth else maxDepth
  visit[v] = False

visit = [False] * (n+1)
isExist = False
for i in range(n+1):
  maxDepth = 0
  dfs(i, 1)
  if maxDepth >= 5:
    isExist = True
    break

if isExist:
  print(1)
else:
  print(0)