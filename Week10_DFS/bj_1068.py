# 백준 1068) 트리
# 입력 : 노드의 개수, 0~N-1번 노드의 부모, 지울 노드의 번호
# 출력 : 리프 노드의 개수

import sys
sys.setrecursionlimit(10**7)
n = int(sys.stdin.readline())
nodes = list(map(int, sys.stdin.readline().split()))
d_node = int(sys.stdin.readline())

tree = [[] for _ in range(n)]
for i in range(n):
  if nodes[i] == -1:
    continue
  tree[nodes[i]].append(i)

deleted = [False] * n
def dfs(v):
  deleted[v] = True
  for w in tree[v]:
    if deleted[w] == False:
      dfs(w)

deleted[d_node] = True
count = 0

for i in range(n):  # 삭제 노드와 연결된 노드 탐색
  if deleted[i] == True:
    continue
  elif i in tree[d_node]:
    dfs(i)

for i in range(n):  # 리프 노드 탐색
  if i == d_node and len(tree[nodes[i]]) == 1:
    count += 1
  elif deleted[i] == True:
    continue
  else:
    if len(tree[i]) == 0:
      count += 1

print(count)