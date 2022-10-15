#l=1 : 1번째 동전 몇개
#l=2 : 2번째 동전 몇개
#l=3 : 3번째 동전 몇개

import sys
sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    global cnt
    if sum>m:
        return
    if L==n:
        if sum==m:
            cnt+=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(cv[L]*i))

m=int(input())
n=int(input())
cv=list()
cn=list()
for i in range(n):
    a, b=map(int, input().split())
    cv.append(a)
    cn.append(b)
cnt=0
DFS(0, 0)
print(cnt)