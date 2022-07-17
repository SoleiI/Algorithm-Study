# 백준 2812) 크게 만들기
# 입력 : 자릿수 N, 지울 숫자 개수 K, N자리 숫자
# 출력 : K개를 지웠을 때 얻을 수 있는 가장 큰 수

import sys
n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().rstrip()))
stack = []

for i in range(n):
  while stack and stack[-1] < num[i] and k > 0:
    stack.pop()
    k -= 1
  
  stack.append(num[i])

print(*stack[:len(stack)-k], sep='')