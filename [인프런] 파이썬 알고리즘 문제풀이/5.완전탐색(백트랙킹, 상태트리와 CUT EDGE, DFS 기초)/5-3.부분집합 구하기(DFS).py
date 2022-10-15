#상태트리: 왼쪽은 O 오른쪽은 X
def DFS(v):
    if v==n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ### 여기가 왼쪽!
        ch[v] = 1
        DFS(v+1)
        ###
        ### 여기가 오른쪽!
        ch[v] = 0
        DFS(v+1)
        ###
n = int(input())
ch = [0]*(n+1)
DFS(1)