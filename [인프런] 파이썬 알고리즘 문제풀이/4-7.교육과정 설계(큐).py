#띄어쓰기 없는 문자열을 리스트에 한 글자 한 글자 나눠 담는법
#print("#%d YES" %(i+1)) 와 같은 표현 기억
#틀려서 질문! 왜 띄어쓰기가 이렇게 되는지?
#입력을 나눠 받게 코드를 작성했는데 통째로 입력했기 때문에 오류 발생
#'수업 설계는 같은 과목을 여러 번 이수하도록 설계해도 됩니다.' 를 잘못 읽음
#str을 deq로 만들 수 있구나.
from collections import deque
s = input()
n = int(input())
lst = []
for i in range(n):
    lst.append(input())

for i, x in enumerate(lst):
    deq = deque(s)
    for v in x:
        if v in deq:
            if deq.popleft() != v:
                print("#%d NO" %(i+1))
                break
    else:
        if len(deq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))