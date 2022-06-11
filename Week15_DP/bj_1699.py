# 백준 1699) 제곱수의 합
# 입력 : 자연수 N
# 출력 : 제곱수 항의 최소 개수

n = int(input())
dp = [0] * (n+1)
square = [i*i for i in range(1, 317)]

for i in range(1, n+1):
  arr = []
  for j in square:
    if j > i:
      break
    arr.append(dp[i-j])
  dp[i] = min(arr) + 1

print(dp[n])