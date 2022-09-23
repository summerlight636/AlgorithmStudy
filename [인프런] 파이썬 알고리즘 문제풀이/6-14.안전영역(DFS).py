#이전 까지는 따로 ch 그래프를 만들지 않았지만,
#이 문제의 경우는 해당 그래프를 여러번 탐색할 것이기 때문에
#원래 그래프를 바꿔 버리면 안되고, ch 그래프를 따로 만들어야 한다.
#100까지 확인하되, board의 값은 변하지 않고 h만 커지면
#h가 커진다고 해서 cnt가 늘어날 수는 없기 때문에
#if cnt == 0: 조건으로 break를 걸어준다.
#import sys
#sys.setrecursionlimit(10**6) 를 해주어야 한다!

import sys

sys.stdin = open("input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sys.setrecursionlimit(10 ** 6)


def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)


if __name__ == "__main__":
    n = int(input())
    cnt = 0
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]
    for h in range(100):
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)
        if cnt == 0:
            break
    print(res)





