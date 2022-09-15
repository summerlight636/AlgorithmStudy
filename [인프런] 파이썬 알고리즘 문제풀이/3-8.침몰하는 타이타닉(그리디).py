#리스트에서 특정 값 x 삭제: a.remove(x)
#for 문에서 중간에 값 삭제하면 원래 인덱스의 값을 가져온다.
#즉 바뀐 리스트에서 인덱스는 그대로
#꼭 m에 최대한 근접하도록 몸무게를 맞출 필요가 없다.
#그냥 제일 작은 몸무게라도 태우면 된다, 왜냐하면 다음 배에 타는 승객은 이전 승객보다 더 가볍기 때문.
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

cnt = 0
while lst:
    x = lst.pop(0)
    cnt += 1
    if len(lst) != 0:
        if lst[-1] + x <= m:
            lst.pop()
print(cnt)

'''
cnt = 0
while lst:
    x = lst.pop(0)
    cnt += 1
    for i, v in enumerate(lst):
        if v <= m-x:
            lst.pop(i)
            break
print(cnt)
'''
