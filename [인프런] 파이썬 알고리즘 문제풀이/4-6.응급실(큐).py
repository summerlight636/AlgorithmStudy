#같은 위험도가 존재할 수 있다 => 구분을 해야함 따라서 인덱스를 지정해준다.
#같은 위험도라도 다른 사람이기 때문에 다른 취급해야 한다. 따라서 내림차순 정렬하면 안된다!
#deq는 슬라이스를 할 수 없구나.
#[x[1] for x in lst] 와 같은 표현 익숙해지기(리스트 컴프리헨션)
from collections import deque

n, m = map(int, input().split())
'''
lst = list(map(int, input().split()))
deq = deque()
for i, v in enumerate(lst):
    deq.append((i, v))
'''
lst = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]
deq = deque(lst)

cnt = 0
while deq:
    if any([deq[0][1]<deq[i][1] for i in range(1, len(deq))]):
        deq.append(deq.popleft())
    else:
        i, v = deq.popleft()
        cnt += 1
        if i == m:
            print(cnt)
            break
