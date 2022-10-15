# a = list(range(1, 21))
# 시작점 s, 끝점 e 로 변수명
# (s+e+1)//2 은 중간 지점 포함X
# (s+e)//2 + 1 은 중간 지점 포함O
# (s+e+1)//2 를 할 게 아니라, (e-s+1)//2 로 단순화해서 했어야 함.
# 인덱스를 굳이 맞춰 줄 필요 없이, 마지막에 arr.pop(0) 을 이용해 첫 공간을 비워버리는 것도 방법이다.
# 값 뒤집기: 첫 값과 끝 값 서로 교환

# 알고리즘
arr = list(range(21))
for _ in range(10):
    # 인덱스를 굳이 맞춰 줄 필요 없이, 마지막에 arr.pop(0) 을 이용해 첫 공간을 비워버리는 것도 방법이다.
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        arr[s+i], arr[e-i] = arr[e-i], arr[s+i]

arr.pop(0)
print(arr)