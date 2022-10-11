# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 노란색 카펫 개수와 갈색 카펫 개수 사이에는 규칙 존재

def solution(brown, yellow):
    n_plus_m = (brown - 4) // 2
    n = n_plus_m - 1

    while True:
        if n * (n_plus_m - n) == yellow:
            break
        else:
            n -= 1

    return [n + 2, n_plus_m - n + 2]