#6-10 미로탐색 문제에서 원래 노드보다 더 높은 값을 가져야 한다는 조건만 추가하면 된다.
import sys
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx, yy)
                ch[xx][yy]=0

if __name__=="__main__":
    n=int(input())
    board=[[0]*n for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    max=-2147000000
    min=2147000000
    for i in range(n):
        tmp=list(map(int, input().split()))
        for j in range(n):
            if tmp[j]<min:
                min=tmp[j]
                sx=i
                sy=j
            if tmp[j]>max:
                max=tmp[j]
                ex=i
                ey=j
            board[i][j]=tmp[j]
    ch[sx][sy]=1
    cnt=0
    DFS(sx, sy)
    print(cnt)