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