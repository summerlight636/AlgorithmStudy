# 가장 마지막 값만 고려하면 되는 경우: 스택!!
def solution(s):
    res = []
    for x in s:
        if len(res) == 0:
            res.append(x)
            continue
        if res[-1] == x:
            res.pop()
        else:
            res.append(x)
    if len(res) == 0:
        return 1
    else:
        return 0

# 참고 답안1
# 조건문에서 not(answer) 라고 표현할 수 있는 것 처음 알았다. 비어있으면 False를 반환한다.
def solution(s):
    answer = []
    for i in s:
        if not (answer):
            answer.append(i)
        else:
            if (answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)
    return not (answer)