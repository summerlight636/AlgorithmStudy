#역으로 사다리를 타야한다!! 출발이랑 도착이랑 고정되어 있으니까.

import sys
sys.stdin=open("input.txt", "r")
def DFS(x, y):
    ch[x][y]=1
    if x==0:
        print(y)
    else:
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)


board=[list(map(int, input().split())) for _ in range(10)]
ch=[[0]*10 for _ in range(10)]
for y in range(10):
    if board[9][y]==2:
        DFS(9, y)