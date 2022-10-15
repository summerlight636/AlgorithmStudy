# 방향 있으면 방향 그래프,
# 가중치가 있으면 가중치 방향 그래프

n=int(input())
m=int(input())
g=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b=map(int, input().split())
    g[a][b]=1
    g[b][a]=1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()