# 감이 안 잡힌다. = 스택이라는 새로운 자료구조를 사용해야 한다.
# 스택: 리스트에서 pop(), append() 만 이용하면 스택 자료구조!
# res=''.join(map(str,stack))
# for x in stack: print(x, end='') 둘다 같은 기능
# 스택으로 내림차순 만들기
# len(stack) == 0 보다는 그냥 if stack: 하면 깔끔하게 표현할 수 있다.
# 입력 예시를 보면서 상수를 그냥 대입해버리는 실수. -2 가 아니라 -m 을 써야 한다.

# 사실 map이 반환하는 맵 객체는 이터레이터라서 변수 여러 개에 저장하는 언패킹(unpacking)이 가능합니다.
# 그래서 a, b = map(int, input().split())처럼 list를 생략한 것입니다('39.2 이터레이터 만들기' 참조).
# a, b = map(int, input().split())을 풀어서 쓰면 다음과 같은 코드가 됩니다.
# x = input().split()    # input().split()의 결과는 문자열 리스트
# m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
# a, b = m               # 맵 객체는 변수 여러 개에 저장할 수 있음

n, m = map(int, input().split())
lst = list(map(int, str(n)))
stack = []

#1. 지금 넣는 수보다 작은 값이 앞에 있으면 삭제
#2. 없으면 넣기
#예외1. 만약 m이 남았다면 마지막 부분에서 슬라이스
for x in lst:
    while stack and stack[-1] < x and m > 0:
        stack.pop()
        m -= 1
    stack.append(x)

if m > 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)
