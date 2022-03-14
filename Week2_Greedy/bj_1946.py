# 백준 1946) 신입 사원
# 입력 : 테스트 케이스 개수, 각 테스트 케이스의 지원자 숫자, 서류심사 성적, 면접 성적 순위
# 출력 : 고용 가능한 최대 인원 수

testcase = int(input())     # 테스트 케이스 수

# 테스트케이스 별 선발 결과
for i in range(testcase):
  applicants = int(input())   # 지원자 수
  scores = []                 # 점수
  for i in range(applicants):
    score1, score2 = map(int, input().split())
    scores.append([score1, score2])

  scores.sort()
  score = scores[0][1]
  result = 1            # 1등은 무조건 합격

  for i in range(len(scores)):
    if scores[i][1] < score:
      score = scores[i][1]
      result += 1

  print(result)