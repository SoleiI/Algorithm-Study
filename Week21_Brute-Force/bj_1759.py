# 백준 1759) 암호 만들기
# 입력 : 암호의 길이 L, 문자의 개수 C, 알파벳 소문자
# 출력 : 사전식으로 가능성 있는 모든 암호

import sys
from itertools import combinations

l, c = map(int, sys.stdin.readline().split())
alphabets = sys.stdin.readline().split()

vowels = ['a', 'e', 'i', 'o', 'u']
keys = []

consonants = []
for i in range(c):
  if not alphabets[i] in vowels:
    consonants.append(alphabets[i])

for key in combinations(alphabets, l):
  key = list(key)

  count = 0
  for c in consonants:
    if c in key:
      count += 1

  if count >= 2:
    for v in vowels:
      if v in key:
        key.sort()
        keys.append(''.join(k for k in key))
        break

keys.sort()
for key in keys:
  print(key)