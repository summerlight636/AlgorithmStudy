#전위순회/후위순회 이런 거 아예 모르겠는데.. ?
#전위순회 부(함수본연의일)-왼-오 ex) 대부분의
#중위순회 왼-부-오
#후위순회 왼-오-부 ex) 병합 정렬
#부=n 왼=2n 오=2n+1
#깊이 우선 탐색의 기본 구조는
# def DFS(v):
# if 종료조건:
# else:
#   print(v))함수본연의일, 즉 부!
#   DFS(v*2) 왼!
#   DFS(v*2+1) 오!

def DFS(v):
    if v>7:
        return
    else:
        print(v)
        DFS(2*v)
        DFS(2*v+1)

'''
중위순회
def DFS(v):
    if v>7:
        return
    else:
        DFS(2*v)
        print(v)
        DFS(2*v+1)
'''


'''
후위순회
def DFS(v):
    if v>7:
        return
    else:
        DFS(2*v)
        DFS(2*v+1)
        print(v)
'''

DFS(1)