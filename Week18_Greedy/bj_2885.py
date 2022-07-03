# 백준 2885) 초콜릿 식사
# 입력 : 정사각형의 개수 K
# 출력 : 가장 작은 초콜릿의 크기, 쪼개야 하는 최소 횟수

k = int(input())

d = 1
while k > d:
  d *= 2

if k == 0:
  choco = 0
else:
  choco = d

count = 0
while k > 0:
  if k == d:
    break
  else:
    while d > k:
      d = d / 2
      count += 1
    k -= d

print(choco, count)