# 백준 12904) A와 B
# 입력 : 두 문자열 S, T
# 출력 : S를 T로 바꿀 수 있는지 여부(1, 0)

s = input()
t = input()

while len(s) != len(t):
  if t[-1] == 'A':
    t = t[:-1]
  else:
    t = t[:-1]
    t = t[::-1]

if s == t:
  print(1)
else:
  print(0)