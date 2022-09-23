#level이 변수에 없는 DFS
#원래 방식대로 하면 time이 항상 n+1에 도착하는 것이 아니기 때문에 케이스를 놓치게 됨
#만족안할 경우 한 단계씩 다음 단계로 가는 DFS(l+1) 이 필요!
#t들이 들어가는 리스트를 대문자로 T 와 같이 표현하는 방법도 직관적이다.

n = int(input())
pt = [0]
pp = [0]
for i in range(n):
    t, p = map(int, input().split())
    pt.append(t)
    pp.append(p)

def DFS(time, sum):
    global max_p
    if time == n+1:
        if sum > max_p:
            max_p = sum
    else:
        if time+pt[time] <= n+1:
            DFS(time+pt[time], sum+pp[i])
        DFS(time+1, sum)

''' 수정 전
def DFS(l, time, sum):
    global max_p
    if l == n:
        ###
        이 구문이 여기 있으면 안된다! 아예 실행이 불가능하기 때문에.
        if time > n:
            return
        ###
        if sum > max_p:
            max_p = sum
    else:
        for i in range(time, n+1):
            if time+pt[i] <= n+1:
                DFS(l+1, time+pt[i], sum+pp[i])
'''

max_p = 0
DFS(1, 0)
print(max_p)