#표현 익숙해지기 all(리스트 컴프리헨션)
#if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):

n = int(input())
mtx = [[0]*(n+2)]
for i in range(n):
    temp = [0] + list(map(int, input().split())) + [0]
    mtx.append(temp)
mtx.append([0]*(n+2))

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if mtx[i][j] > mtx[i-1][j] and mtx[i][j] > mtx[i+1][j] and mtx[i][j] > mtx[i][j-1] and mtx[i][j] > mtx[i][j+1]:
            cnt += 1

print(cnt)

#정답
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)): #표현 익숙해지기 all(리스트 컴프리헨션)
            cnt+=1
print(cnt)