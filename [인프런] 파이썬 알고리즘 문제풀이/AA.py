#포인터 잡을때 lt, rt 와 같이 잡는다. (무조건 lt < rt 이기 때문)
#p1, p2 와 같이 잡을 때에는 서로 대소관계가 유지되지 않는 경우에 쓴다.

n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for lt in range(n):
    rt = lt + 1
    tot = 0
    while tot < m and rt <= n:
        tot = sum(a[lt:rt])
        if tot == m:
            cnt += 1
            break
        rt += 1

print(cnt)