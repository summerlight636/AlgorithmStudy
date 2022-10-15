#상태 트리라고 생각을 안하니까, if l==n : 이 생각이 안났다.
#5개를 다 써야하는 게 아니니까. 착각 조심.
#pv, pt 를 한 리스트에 안 넣고, 따로 리스트를 만드는 발상

n, m = map(int, input().split())
pv = []
pt = []
for i in range(n):
    s, t = map(int, input().split())
    pv.append(s)
    pt.append(t)

def DFS(l, sum, time):
    global res
    if l == n:
        if time > m:
            return
        if sum > res:
            res = sum
    else:
        DFS(l+1, sum+pv[l], time+pt[l])
        DFS(l+1, sum, time)

res = 0
DFS(0, 0, 0)
print(res)