# 백준 1931) 회의실 배정
# 입력 : 회의의 수, 회의의 정보(시작시간, 끝나는 시간)
# 출력 : 사용할 수 있는 회의의 최대 개수

import sys
meetingNum = int(input())
meetings = []
for i in range(meetingNum):
  meetings.append(tuple(map(int, sys.stdin.readline().split())))

meetings.sort(key=lambda x:x[0])  # 시작 시간 기준으로 정렬
meetings.sort(key=lambda x:x[1])  # 끝나는 시간 기준으로 정렬

possibleMeetings = []
possibleMeetings.append(meetings[0])
lastTime = meetings[0][1]

for i in range(1, len(meetings)):     # 두번째 원소부터 순회
  if meetings[i][0] >= lastTime:      # lastTime보다 시작 시간이 같거나 뒤면 append
    possibleMeetings.append(meetings[i])
    lastTime = meetings[i][1]         # lastTime을 meeting의 끝나는 시간으로 변경

print(len(possibleMeetings))