#5/5, 10분
#마지막에 한 번 출력하는 cnt는 어떻게 처리하는 게 효율적일까? 나 처럼 cnt는 전역변수로 지정
#리스트 str로 간단하게 표현하는 방법
#이진트리가 아닌, n가닥 으로 뻗어나가는 트리!
#import sys
#input = sys.stdin.readline
#s=input().rstrip() #문자열을 입력받을 때는 줄바꿈 기호를 제거해주어야 한다.


n, m = map(int, input().split())

def DFS(l, result):
    global cnt
    if l == m:
        cnt += 1
        for x in result:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            '''
            그냥 이부분을
            result[l] = i
            DFS(l+1) 
            으로 간단히 할 수도 있다.
            이 경우 DFS() 의 변수가 level밖에 없어 깔끔하게 작성할 수 있다. 
            '''
            result.append(i)
            DFS(l+1, result)
            result.pop()

cnt = 0
DFS(0, [])
print(cnt)