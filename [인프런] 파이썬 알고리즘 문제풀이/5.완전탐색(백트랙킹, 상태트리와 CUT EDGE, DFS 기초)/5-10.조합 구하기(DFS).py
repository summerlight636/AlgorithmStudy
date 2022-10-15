#중요한 문제 => 응용이 많다.
#조합은 DFS에 시작 숫자 s변수가 필요하다. (시작 변수 이후에서만 다음 값 가져올 수 있게!)

def DFS(l, s):
    global cnt
    if l == m:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for i in range(s, n+1):
            res[l] = i
            DFS(l+1, res[l]+1)


n, m = map(int, input().split())
res = [0]*m
cnt = 0
DFS(0, 1)
print(cnt)
