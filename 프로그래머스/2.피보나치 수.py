#https://school.programmers.co.kr/learn/courses/30/lessons/12945
#재귀 한도를 푸는 방법 알아두기

import sys
sys.setrecursionlimit(10**7)

lst = [-1]*100001
lst[0] = 0
lst[1] = 1

def solution(n):
    if n == 0: return 0
    if n == 1: return 1
    if lst[n] != -1:
        return lst[n]
    lst[n] = (solution(n-1) + solution(n-2)) % 1234567
    return lst[n]