#이게 왜 BFS 문제인지 부터 모르겠다.
#중심으로부터 상하좌우로 퍼진다. => 마름모 형태로 퍼진다.

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
sum = 0
Q = deque()
ch[n // 2][n // 2] = 1
sum += a[n // 2][n // 2]
Q.append((n // 2, n // 2))
L = 0
while True:
    if L == n // 2:
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            #방문 안한 곳만 다시 체크해야한다!
            if ch[x][y] == 0:
                sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1
print(sum)

