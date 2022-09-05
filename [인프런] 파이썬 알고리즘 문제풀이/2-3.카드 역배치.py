# a = list(range(1, 21))
# 시작점 s, 끝점 e 로 변수명
# (s+e+1)//2 은 중간 지점 포함X
# (s+e)//2 + 1 은 중간 지점 포함O

# 시간 1:07 -


# 알고리즘
arr = list(range(1, 21))
for _ in range(10):

    ai, bi = map(int, input().split())
    arr[ai-1:bi] = arr[ai-1:bi:-1]
print(arr)