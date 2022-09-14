#리스트에서 특정 값 x 삭제: a.remove(x)
#for 문에서 중간에 값 삭제하면 원래 인덱스의 값을 가져온다.
#즉 바뀐 리스트에서 인덱스는 그대로
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

cnt = 0
while lst:
    x = lst.pop(0)
    cnt += 1
    for i, v in enumerate(lst):
        if v <= m-x:
            lst.pop(i)
            break
print(cnt)