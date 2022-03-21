# 백준 1339) 단어 수학
# 입력 : 단어 개수, 알파벳 대문자로 이루어진 단어
# 출력 : 주어진 단어의 합의 최대값

import sys
words = int(sys.stdin.readline())
alphabets = [[chr(65+i), 0] for i in range(26)] # [['A', 0], ['B', 0], ... , ['Z', 0]]

for i in range(words):
  word = sys.stdin.readline().rstrip()
  for i in range(len(word)):
    alphabets[ord(word[i])-65][1] += 10 ** (len(word)-1-i)

alphabets.sort(key=lambda x:x[1], reverse=True) # 자릿수 기준으로 정렬

sum = 0
for i in range(10):   # 10개의 알파벳만 들어가므로
  sum += (9-i) * alphabets[i][1]

print(sum)