# https://school.programmers.co.kr/learn/courses/30/lessons/12941

# 그냥 최솟값과 최댓값 단순하게 곱해주면 되는 건데. 잘못 생각해서 복잡하게 코드를 썼다.

# 더 간단하게 표현

def solution(A, B):
    A = sort()
    B = sort(reverse=True)

    answer = 0
    for i, j in zip(A, B):
        answer += i * j
    return answer


# 내 코드
from collections import deque


def solution(A, B):
    A = deque(sorted(list(map(int, A))))
    B = deque(sorted(list(map(int, B)), reverse=True))

    answer = 0
    while A:
        if A[0] * B[0] < A[-1] * B[-1]:
            answer += A[0] * B[0]
            A.popleft()
            B.popleft()

        else:
            answer += A[-1] * B[-1]
            A.pop()
            B.pop()

    return answer