# a = list(range(1, 21))
# 시작점 s, 끝점 e 로 변수명
# (s+e+1)//2 은 중간 지점 포함X
# (s+e)//2 + 1 은 중간 지점 포함O
# (s+e+1)//2 를 할 게 아니라, (e-s+1)//2 로 단순화해서 했어야 함.


# 알고리즘
arr = list(range(1, 21))
for _ in range(10):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    for i in range((e-s+1)//2):
        arr[s+i], arr[e-i] = arr[e-i], arr[s+i]
print(arr)