#최대힙은 최소힙에서 push 할 때와 pop할 때의 부호만 바꾸어 주면 된다.
import heapq as hq
lst = []
while True:
    n = int(input())
    if n > 0:
        hq.heappush(lst, -n)
    elif n == 0:
        if len(lst) == 0:
            print(-1)
        else:
            print(-hq.heappop(lst))
    else:
        break