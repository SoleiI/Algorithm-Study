# 백준 14889) 스타트와 링크
# 입력 : 축구를 하기 위해 모인 사람의 수(N), 능력치(S)
# 출력 : 스타트 팀과 링크 팀의 능력치 차이의 최솟값

from sys import stdin
n = int(input())
s = [list(map(int, stdin.readline().split())) for _ in range(n)]

start = []    # 스타트 팀 경우의 수
link = []     # 링크 팀 경우의 수
temp = [0]    # 0이 들어간 구성으로만 팀을 짜면 전체 경우의 수의 절반의 경우가 나옴
nums = [_ for _ in range(n)]  # [0, 1, 2, ..., n-1]

# 팀 나누기
def buildTeam(a, temp):
  for i in range(a+1, n):
    temp.append(i)
    if len(temp) == n / 2:
      start.append(list(temp))
      link.append(list(set(nums)-set(temp)))
    else:
      buildTeam(i, temp)
    temp.pop()

# 각 팀의 능력치 합 구하기
def getTeamStats(arr):
  sum = 0
  for i in arr:
    for j in arr:
      sum += s[i][j]
  return sum

# 최솟값 구하기
minDiff = 1000

buildTeam(0, temp)
for i in range(len(start)):
  diff = abs(getTeamStats(start[i]) - getTeamStats(link[i]))
  minDiff = min(minDiff, diff)

print(minDiff)
