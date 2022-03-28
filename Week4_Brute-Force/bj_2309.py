# 백준 2309) 일곱 난쟁이
# 입력 : 아홉 난쟁이들의 키
# 출력 : 합이 100이 되는 일곱 난쟁이들의 키

import sys
sum = 0           # 아홉 난쟁이들의 키 합
heights = []      # 아홉 난쟁이들의 키 리스트
for i in range(9):
  height = int(sys.stdin.readline())
  sum += height
  heights.append(height)
heights.sort()

def printHeights(n, m):
  for h in heights:
    if h != n and h != m:
      print(h)

for h in heights:
  sumOfEight = sum - h  # h를 제외한 나머지 합
  if sumOfEight > 100:
    rest = sumOfEight-100 # h와 함께 주인공이 아닌 난쟁이의 키
    if rest in heights:
      printHeights(h, rest)
      break