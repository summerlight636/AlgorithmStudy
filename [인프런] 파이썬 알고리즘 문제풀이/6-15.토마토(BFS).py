#처음 큐에 넣을 때 모든 토마토의 좌표(예시에서는 2개)를 몽땅 큐에 넣어야 한다. #
#동시에 퍼지기 때문!
#ch보다 더 자세한건 dis(거리=시간).
#여기서는 단순히 방문 완료의미가 아니라, 시간을 요구하기 때문에 dis가 적절하다.

import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n, m=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(m)]
Q=deque()
dis=[[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if board[i][j]==1:
            Q.append((i, j))
while Q:
    x, y=Q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and board[nx][ny]==0:
            board[nx][ny]=1
            dis[nx][ny]=dis[x][y]+1
            Q.append((nx, ny))
flag=1
for i in range(m):
    for j in range(n):
        if board[i][j]==0:
            flag=0
result=0
if flag==1:
    for i in range(m):
        for j in range(n):
            if dis[i][j]>result:
                result=dis[i][j]
    print(result)
else:
    print(-1)