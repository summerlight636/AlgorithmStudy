import sys
#sys.exit(0) : 아예 프로그램을 종료 시켜버린다.
#DFS(level, 매개변수) 사용하는 법 익숙해지기.
#이전 단계(level)의 결과가 그대로 다음 단계에 영향을 줄 때 매개변수로 넘겨주자.
#나눠진 두 값이 같다: sum == total-sum 과 같이 표현하는 게 제일 깔끔하다.
#if sum>total//2: return 추가
def DFS(l, sum):
    if sum>total//2:
        return
    if l == n:
        if sum == total - sum:
            print("YES")
            sys.exit(0)
    else:
        DFS(l+1, sum+lst[l]) #상태트리의 왼쪽으로 이동
        DFS(l+1, sum) #상태트리의 오른쪽으로 이동

n = int(input())
lst = list(map(int, input().split()))
total = sum(lst)
DFS(0, 0)
print("NO")

''' 내 코드 
#YES 여러번 출력되어 실패 - sys.exit(0) 적용하여 해결
#//2 를 이용하려고 해서, 불필요한 조건들이 생겨나 복잡해 보인다. 
#sum(lst)는 불변이기 때문에 메인 코드에서 한 번만 계산해주자. 
#sum 변수를 이용하지 않더라도 풀 수는 있지만, 
#상태 체크 리스트 ch 가 추가로 필요하고, 
#ch를 한 바퀴 더 확인해주는 작업이 필수적이 됨. 
def DFS(v):
    if v==n:
        temp_sum = 0
        for i in range(n):
            if ch[i] == 1:
                temp_sum += lst[i]
        if temp_sum == sum(lst)//2:
            print("YES")
            sys.exit(0)
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)

n = int(input())
lst = list(map(int, input().split()))
ch = [0]*n

if sum(lst) % 2 != 0:
    print("NO")

else:
    DFS(0)
    print("NO")
'''

