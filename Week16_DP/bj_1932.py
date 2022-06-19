# 백준 1932) 정수 삼각형
# 입력 : 삼각형의 크기 n, 정수 삼각형
# 출력 : 합이 최대가 되는 경로에 있는 수의 합

import sys
n = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = list([0] * i for i in range(1, n+1))

for i in range(n):
  for j in range(i+1):
    if j-1 < 0:
      dp[i][j] = triangle[i][j] + dp[i-1][j]
    elif j > i-1:
      dp[i][j] = triangle[i][j] + dp[i-1][j-1]
    else:
      dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
