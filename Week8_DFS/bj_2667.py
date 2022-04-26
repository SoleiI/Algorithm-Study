# 백준 2667) 단지번호붙이기
# 입력 : 지도의 크기 N, N개의 0 또는 1
# 출력 : 총 단지 수, 각 단지 내 집 수 오름차순 정렬

n = int(input())
map = [list(map(int, input())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]

def recursive_dfs(i, j, complex):
  if map[i][j] == 1:
    visit[i][j] = True
    complex.append([i, j])
    if j+1 < n and visit[i][j+1] == False and map[i][j+1] == 1:
      recursive_dfs(i, j+1, complex)   # 오른쪽

    if i+1 < n and visit[i+1][j] == False and map[i+1][j] == 1:
      recursive_dfs(i+1, j, complex)   # 위쪽
    
    if j > 0 and visit[i][j-1] == False and map[i][j-1] == 1:
      recursive_dfs(i, j-1, complex)   # 왼쪽
    
    if i > 0 and visit[i-1][j] == False and map[i-1][j] == 1:
      recursive_dfs(i-1, j, complex)   # 아래쪽
  return complex

houses = []
for i in range(n):
  for j in range(n):
    if visit[i][j]:
      continue
    count = len(recursive_dfs(i, j, []))
    if count > 0: houses.append(count)

houses.sort()
print(len(houses))
for i in houses:
  print(i)
