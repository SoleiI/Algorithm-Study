# 백준 1463) 1로 만들기
# 입력 : 정수 N
# 출력 : 연산을 하는 횟수의 최솟값

n = int(input())
dp = [0] * 1000001

for i in range(2, n+1):
  dp[i] = dp[i-1] + 1
  if i % 6 == 0:
    dp[i] = min(dp[i//2]+1, dp[i//3]+1)
  elif i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3]+1)
  elif i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])