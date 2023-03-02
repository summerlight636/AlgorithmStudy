#https://velog.io/@rltjr1092/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%94%BC%EB%A1%9C%EB%8F%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4
#참고 답안2
answer = 0
visited = []


def enter(dungeons, k, i):
    global answer
    k -= dungeons[i][1]
    answer = max(answer, sum(visited))

    for j in range(len(dungeons)):
        if not visited[j] and dungeons[j][0] <= k:
            visited[j] = 1
            enter(dungeons, k, j)
            visited[j] = 0


def solution(k, dungeons):
    global visited
    visited = [0] * len(dungeons)

    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            visited[i] = 1
            enter(dungeons, k, i)
            visited[i] = 0
    return answer


# 1. 그리디로 풀 수 있는 문제 인가?
# 증명 방법 공부하기
# 2. k 값이 작아서 완전탐색해도 되겠다.

#참고 답안3
answer = 0
def enter(dungeons, k, i, visited):
    global answer
    visited = visited[:]
    visited[i] = 1
    k -= dungeons[i][1]
    answer = max(answer, sum(visited))

    for j in range(len(dungeons)):
        if not visited[j] and dungeons[j][0] <= k:
            enter(dungeons, k, j, visited)

def solution(k, dungeons):
    visited = [0] * len(dungeons)

    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            enter(dungeons, k, i, visited)

    return answer

answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    # 그냥 최적의 answer 를 찾는 것이기 때문에 종료조건 없이, 갱신만 해주면 됨 
    if cnt > answer:
        answer = cnt

    # 이미 다녀온 던전을 표현하기 위해서 idx를 일일이 튜플로 저장해두려고 했는데 .. 
    # 이렇게 하면 표현이 복잡해져서 실수가 생기는 단점.   
    # 그냥 idx 순서 같은 것을 이용해서 visited 리스트를 만들어서 사용하면 더 깔끔하다 
    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

# def dfs(a, piro):
#     if a == len(dungeons) or piro < min([x[1][0] for x in idx_dungeons])
#         if answer < cnt:
#             answer = cnt
#     else:
#         idx_dungeons = [x for x in idx_dungeons if x[1][0]<=k]
#         for i, dungeon in idx_dungeons: 
#             dfs(a+1, k-dungeon[1])

# def solution(k, dungeons):
#     idx_dungeons = []
#     for i,x in enumerate(dungeons):
#         idx_dungeons.append((i, x))
#     answer = -1
#     dfs(0, k)
#     return answer