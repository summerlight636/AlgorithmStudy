# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    for i in range(1, (n + 1) // 2):
        temp = i
        while temp < n:
            i += 1
            temp += i
        if temp == n:
            answer += 1

    return answer + 1