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

# 다시 풀기
# 최소힙 다루는 법
# import heapq as hq (from collections 아님)
# lst = [] 라고 선언 후, hq.heappush() 랑 hq.heappop()만으로 값을 입력, 출력하면 된다.
# 1:08 ~ 1:14

import heapq as hq

lst = []
while True:
    a = int(input())
    if a>0:
        hq.heappush(lst, a)
    elif a==0:
        if lst:
            print(hq.heappop(lst))
        else:
            print(-1)
    elif a==-1:
        break

