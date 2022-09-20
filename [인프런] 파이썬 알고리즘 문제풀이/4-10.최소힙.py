#최소힙 사용하기:
#리스트에서 heapq를 import하여 heappush, heappop만으로 값을 입력, 출력하면 된다.
import heapq as hq
lst = []
while True:
    n = int(input())
    if n > 0:
        hq.heappush(lst, n)
    elif n == 0:
        if len(lst) == 0:
            print(-1)
        else:
            print(hq.heappop(lst))
    else:
        break