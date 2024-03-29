#BFS는 deque로.
#즉석으로 리스트 같이 표현하기 for next in (now - 1, now + 1, now + 5):
#최단 경로는 BFS로! 먼저 구한 노드가 더 최단 경로일 수 밖에 없다.

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in (now - 1, now + 1, now + 5):
        if 1 <= next <= MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1

print(dis[m])