#6-12와 완전히 같은 문제, 8방향 인 것만 다르다. BFS로 풀이하는 연습만~

import sys
from collections import deque
sys.stdin=open("input.txt", "r")
dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]
n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
cnt=0
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i, j))
            while Q:
                tmp=Q.popleft()
                for k in range(8):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y]==1:
                        board[x][y]=0
                        Q.append((x, y))
            cnt+=1
print(cnt)
