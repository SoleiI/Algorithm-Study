# 백준 2606) 바이러스
# 입력 : 컴퓨터 수, 직접 연결된 컴퓨터 쌍의 수, 직접 연결된 컴퓨터의 번호 쌍
# 출력 : 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수

import sys
computers = int(input())
connections = int(input())

graph = [[] for _ in range(computers)]

for _ in range(connections):
  a, b = map(int, sys.stdin.readline().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)

visit = []
def recursive_dfs(v):
  global count
  visit.append(v)
  for w in graph[v]:
    if not w in visit:
      recursive_dfs(w)
      count += 1

if __name__ == '__main__':
  count = 0
  recursive_dfs(0)
  print(count)