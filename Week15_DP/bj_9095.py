# 백준 9095) 1, 2, 3 더하기
# 입력 : 테스트 케이스의 개수 T, 정수 n
# 출력 : n을 1, 2, 3의 합으로 나타내는 방법의 수

t = int(input())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
  n = int(input())
  print(dp[n])