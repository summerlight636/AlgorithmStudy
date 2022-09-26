from typing import List
from collections import deque

def fire_bfs(x, y, n, m, graph):
    dx=[-1, -1, 0, 1, 1, 1, 0, -1]
    dy=[0, 1, 1, 1, 0, -1, -1, -1]
    graph[x][y] += m
    ch=[[0]*n for _ in range(n)]
    dis=[[0]*n for _ in range(n)]
    Q=deque()
    Q.append((x, y))
    while Q:
        x, y=Q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0:
                ch[nx][ny]=1
                dis[nx][ny]=dis[x][y]+1
                graph[nx][ny] += m-dis[x][y]
                Q.append((nx, ny))
        if dis[x][y] == m-1:
            break

def ice_bfs(x, y, n, m, graph):
    dx=[-1, 0, 1, 0]
    dy=[0, 1, 0, -1]
    graph[x][y] -= m
    ch=[[0]*n for _ in range(n)]
    dis=[[0]*n for _ in range(n)]
    Q=deque()
    Q.append((x, y))
    while Q:
        x, y=Q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0:
                ch[nx][ny]=1
                dis[nx][ny]=dis[x][y]+1
                graph[nx][ny] -= m-dis[x][y]
                Q.append((nx, ny))
        if dis[x][y] == m-1:
            break

n = 3
m = 2
fires = [[1, 1]]
ices = [[3, 3]]
def solution():
    graph = [[0]*n for _ in range(n)]
    for x, y in fires:
        fire_bfs(x-1,y-1, n, m, graph)
    for x, y in ices:
        ice_bfs(x-1,y-1, n, m, graph)
    return graph

print(solution())