#deque는 원순열을 표현하기에도 적합하다. popleft 후 바로 붙이면~

from collections import deque

n, k = map(int, input().split())

deq = deque(list(range(1, n+1)))
while len(deq) > 1:
    for _ in range(k-1):
        deq.append(deq.popleft())
    deq.popleft()

print(deq[0])
