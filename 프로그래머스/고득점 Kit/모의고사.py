#파이썬으로 리스트를 무한히 순환하고싶을때 ( 일정 패턴을 반복해서 처리하고 싶을때 ) 유용한 cycle 함수 + next 함수 활용하기

#내 풀이
def solution(answers):
    cnt = [0, 0, 0]
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [2, 1, 2, 3, 2, 4, 2, 5]
    lst3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, x in enumerate(answers):
        if lst1[i % 5] == x:
            cnt[0] += 1
        if lst2[i % 8] == x:
            cnt[1] += 1
        if lst3[i % 10] == x:
            cnt[2] += 1

    return [i + 1 for i, x in enumerate(cnt) if x == max(cnt)]

#참고 답안
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]