#재귀함수로 탐색할 때 함수이름을 DFS로.
#거꾸로 출력하려면 호출 밑으로 내려주면 거꾸로 출력된다. (스택을 사용하는 것이므로)
#안했던 일을 하러 다시 온다는 의미에서 백트래킹이라고도 한다.
n = int(input())
def DFS(n):
    if n==0:
        return
    else:
        DFS(n//2)
        print(n%2, end='')
DFS(n)
