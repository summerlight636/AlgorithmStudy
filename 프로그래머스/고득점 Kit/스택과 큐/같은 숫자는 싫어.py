def solution(arr):
    answer = []
    for x in arr:
        if answer == [] or answer[-1] != x:
            answer.append(x)

    return answer


# 참고 답안
# answer[-1:] == [x] 라는 표현이 신박했다.
# 이렇게 하면 answer[-1] 이 존재하지 않아서 발생하는 오류를 미리 처리할 수 있다.
def no_continuous(s):
    answer = []
    for x in s:
        if answer[-1:] == [x]: continue
        answer.append(x)
    return answer

