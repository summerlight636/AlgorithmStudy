#def 안에 def 가능

result = 0

def solution(k, dungeons):
    visited = [0] * len(dungeons)
    dungeons.sort(key=lambda x: (-x[0], -x[1]))
    global result

    def dfs(level, pirodo, cnt):
        global result
        if result < cnt:
            result = cnt
        if level != len(dungeons):
            for i, dungeon in enumerate(dungeons):
                if visited[i] == 0:
                    visited[i] = 1
                    need, use = dungeon
                    if pirodo >= need:
                        dfs(level + 1, pirodo - use, cnt + 1)
                    visited[i] = 0

    dfs(0, k, 0)
    return result