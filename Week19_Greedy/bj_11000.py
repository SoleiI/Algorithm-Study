# 백준 11000) 강의실 배정
# 입력 : 수업의 개수 N, 각 수업의 시작 시간 Si, 종료 시간 Ti
# 출력 : 강의실의 개수

import sys
import heapq  # 가장 작은 원소부터 정렬
n = int(sys.stdin.readline())
classes = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
classes.sort()

classrooms = []
heapq.heappush(classrooms, classes[0][1])
for i in range(1, n):
  if classes[i][0] < classrooms[0]:
    heapq.heappush(classrooms, classes[i][1])
  else:
    heapq.heappop(classrooms) # 가장 작은 원소 삭제
    heapq.heappush(classrooms, classes[i][1])

print(len(classrooms))