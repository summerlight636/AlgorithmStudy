# print(#%d %d" %(i+1, lst[k-1])) 과 같이 출력(문자열 포맷)!

T = int(input())

for i in range(T):
    n, s, e, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = lst[s-1:e]
    lst.sort()
    print("#%d %d" %(i+1, lst[k-1]))