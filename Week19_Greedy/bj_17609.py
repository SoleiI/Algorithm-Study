# 백준 17609) 회문
# 입력 : 문자열의 개수 T, 알파벳 소문자로 이루어진 문자열
# 출력 : 회문(0), 유사회문(1), 일반 문자열(2) 중 해당하는 숫자

import sys
t = int(sys.stdin.readline())
str_list = [sys.stdin.readline().rstrip() for _ in range(t)]

for str in str_list:
  count = 0
  if str != str[::-1]:
    for i in range(len(str) // 2 + 1):
      if str[i] != str[len(str)-1-i]:
        left = str[:i] + str[i+1:]
        right = str[:len(str)-1-i] + str[len(str)-i:]
        if left == left[::-1]:
          count = 1
        elif right == right[::-1]:
          count = 1
        else:
          count = 2
      if count > 0:
        break
  
  print(count)