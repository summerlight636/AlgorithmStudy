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