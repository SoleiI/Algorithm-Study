# 백준 10974) 모든 순열
# 입력 : N
# 출력 : 1부터 N까지의 수로 이루어진 모든 순열

n = int(input())
nums = list(i+1 for i in range(n))      # 숫자
isUsed = list(False for i in range(n))  # 사용 여부
pers = []                               # 모든 순열
temp = []                               # pers에 넣을 순열 임시

def generatePermutation(n):
  for i in range(n):
    if isUsed[i] == True:
      continue
    else:
      temp.append(nums[i])
      isUsed[i] = True
      generatePermutation(n)
      if len(temp) == n:
        pers.append(list(temp))

    temp.pop()
    isUsed[i] = False

generatePermutation(n)

for per in pers:
  print(' '.join(str(x) for x in per))