#money 리스트를 만들어서 각 단계에서 각 사람이 얼마씩 들고 있는지 계산

import sys
sys.stdin = open("input.txt", 'r')
def DFS(L):
    global res
    if L==n:
        cha=max(money)-min(money)
        if cha<res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]

if __name__=="__main__":
    n=int(input())
    coin=[]
    tmp=[]
    money=[0]*3
    res=2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)