# 백준 1062) 가르침
# 입력 : 단어의 개수 N, 글자의 개수 K, 남극 언어의 단어
# 출력 : 학생들이 읽을 수 있는 단어 개수의 최댓값

import sys
from itertools import combinations
n, k = map(int, sys.stdin.readline().split())
letters = ['a', 'n', 't', 'i', 'c']

def preprocess(w):
  word = w[4:-4]
  word = ''.join(set(word))
  for j in word:
    if j in letters:
      index = word.index(j)
      word = word[:index] + word[index+1:]
  return word

words = []
anta = 0
for _ in range(n):
  word = sys.stdin.readline().rstrip()
  if len(word) == 0:
    anta += 1
  words.append(preprocess(word))

words.sort(key=len)

if k == 26:
  print(n)
  exit(0)

k -= 5
if k < 0:
  print(0)
  exit(0)

alphabets = []
for word in words:
  for w in word:
    alphabets.append(w)

alphabets = list(set(alphabets))

max = 0
if k > len(alphabets):
  k = len(alphabets)

for letter in combinations(alphabets, k):
  count, known = 0, True
  for word in words:
    for w in word:
      if not w in letter:
        known = False
    if known:
      count += 1
  
  max = count if count > max else max

print(max+anta)