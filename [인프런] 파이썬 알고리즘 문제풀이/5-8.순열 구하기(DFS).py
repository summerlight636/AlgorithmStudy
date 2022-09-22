#DFS는 해당 노드에서 다음 노드로 갈 때 무엇을 해주어야 하는지 이걸 잘 시뮬레이션하는게 제일 중요한 듯!


def DFS(l):
    global cnt
    if l == m:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                DFS(l+1)
                ch[i] = 0

n, m = map(int, input().split())
ch = [0]*(n+1)
cnt = 0
DFS(0)
print(cnt)
