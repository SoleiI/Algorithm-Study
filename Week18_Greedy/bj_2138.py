# 백준 2138) 전구와 스위치
# 입력 : 전구의 개수 N, 전구들의 현재 상태
# 출력 : 스위치를 누르는 최소 횟수

import sys
n = int(sys.stdin.readline())
initial = list(map(int, sys.stdin.readline().rstrip()))
final = list(map(int, sys.stdin.readline().rstrip()))

def change(x):
  if x == 0:
    return 1
  else:
    return 0

result = 0
for i in range(2):
  count = 0
  temp = list(initial)

  if i == 0:
    count = 1
    temp[0] = change(temp[0])
    temp[1] = change(temp[1])

  for j in range(1, n):
    if temp[j-1] != final[j-1]:
      count += 1
      temp[j-1] = change(temp[j-1])
      temp[j] = change(temp[j])
      if j < n-1:
        temp[j+1] = change(temp[j+1])
  
  if temp == final:
    if result <= 0:
      result = count
    else:
      result = min(result, count)
  else:
    result = -1 if result == 0 else result

print(result)