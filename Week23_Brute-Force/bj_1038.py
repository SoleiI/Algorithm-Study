# 백준 1038) 감소하는 수
# 입력 : N
# 출력 : N번째 감소하는 수

import math
from itertools import combinations

n = int(input())
d_count = [9]
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if n == 0:
  print(0)
elif n > 1022:
  print(-1)
else:
  for i in range(2, 11):
    d_count.append(int(math.factorial(10)/(math.factorial(i) * math.factorial(10-i))))

  index = 0
  for i in range(10):
    if n <= sum(d_count[:i]):
      break
    index = i

  d_nums = []
  if index == 0:
    d_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  else:
    for num in combinations(nums, index+1):
      d_nums.append(int(''.join(sorted(num, reverse=True))))

  d_nums.sort()

  idx = n - sum(d_count[:index])

  print(d_nums[idx-1])