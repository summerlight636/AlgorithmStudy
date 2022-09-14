#from collections import deque 어디서 임포트해야하는 지 알아둘 것
from collections import deque
n = int(input())
lst = list(map(int, input().split()))
deq = deque(lst)

prev = 0
while deq:
    lt = deq[0]
    rt = deq[-1]

    if prev > lt and prev > rt:
        break
    else:
        if prev < rt < lt or lt < prev < rt:
            prev = rt
            deq.pop()
            print('R', end='')
        else:
            prev = lt
            deq.popleft()
            print('L', end='')