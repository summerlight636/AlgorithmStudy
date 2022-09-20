#from collections import deque 어디서 임포트해야하는 지 알아둘 것
#deque는 앞 뒤 양쪽 방향에서 추가, 삭제가 엄청 빠르다.
#왼쪽 끝 ~ 오른쪽 끝 이걸 보면 lt, rt 를 이용해서 포인터를 옮기는 방식을 생각해볼 수 있겠다.
#마지막 하나 남은 건 왼쪽으로 보냐, 오른쪽으로 보냐는 어떤 if를 먼저 쓰느냐로 처리해줄 수 있다.
#tmp = [] 로 하지말고, tmp = []는 맨 처음에만 선언하고 루프 마지막에서 tmp.clear() 를 이용해서 초기화 시켜주는 방법이 더 직관적이다.
from collections import deque
n = int(input())
lst = list(map(int, input().split()))
deq = deque(lst)


prev = 0
res = ""
temp = []
while deq:
    if prev < deq[0]:
        temp.append((deq[0], 'L'))
    if prev < deq[-1]:
        temp.append((deq[-1], 'R'))
    if len(temp) == 0:
        break
    else:
        temp.sort()
        res += temp[0][1]
        prev = temp[0][0]
        if temp[0][1] == 'L':
            deq.popleft()
        else:
            deq.pop()
    temp.clear()
print(len(res))
print(res)
'''
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
'''
