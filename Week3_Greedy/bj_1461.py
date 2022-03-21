# 백준 1461) 도서관
# 입력 : 전체 책의 개수, 한 번에 들 수 있는 책의 개수, 책의 위치
# 출력 : 책을 모두 제자리에 놔둘 때 드는 최소 걸음

import sys
n, m = map(int, sys.stdin.readline().split()) # 책 개수
location = list(map(int, sys.stdin.readline().split())) # 책 위치
steps = 0   # 걸음 수

location.append(0)
location.sort()

origin = location.index(0)
left, right = location[:origin], location[origin+1:]
right.reverse()   # 코드의 재사용성을 높이기 위해 right은 뒤집어 준다.

def countSteps(list):
  count = 0
  if len(list) < m:     # 한 번에 옮길 수 있는 책의 개수보다 적을 경우
    count += list[0]    # 가장 큰 수 더하기
  else:
    for i in range(0, len(list), m):
      count += list[i]
  return abs(count) * 2     # 왔다갔다 하므로 *2

if len(left) == 0:
  steps += countSteps(right)
elif len(right) == 0:
  steps += countSteps(left)
else:
  steps += countSteps(left) + countSteps(right)

if abs(location[0]) > abs(location[-1]):  # 절대값 비교
  steps -= abs(location[0])
else:
  steps -= abs(location[-1])

print(steps)