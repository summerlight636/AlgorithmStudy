#파스칼 삼각형이 이항정리를 이용한다는 것 자체를 까먹었다.
#이항계수 표현
#for i in range(1, n):
#b[i] = b[i-1]*(n-i)/i

import sys

def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum + (p[L] * b[L]))
                ch[i] = 0

n, f = map(int, input().split())
p = [0] * n
b = [1] * n
ch = [0] * (n + 1)
for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i
DFS(0, 0)


''' 내 코드
import sys
def get_sum(lst):
    if len(lst) == 1:
        return lst[0]

    res = []
    for i in range(len(lst)-1):
       res.append(lst[i]+lst[i+1])

    return get_sum(res)

def DFS(l):
    if l == n:
        if get_sum(lst) == f:
            for x in lst:
                print(x, end=' ')
            print()
            sys.exit(0)
    else:
        for i in range(1, n+1):
            if not i in lst:
                lst.append(i)
                DFS(l+1)
                lst.remove(i)

n, f = map(int, input().split())
lst = []
DFS(0)
'''
