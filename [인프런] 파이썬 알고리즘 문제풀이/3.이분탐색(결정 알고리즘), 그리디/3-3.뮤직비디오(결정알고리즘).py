#바로바로 lt, rt 조건이 튀어나오지 않아 오래걸렸다.
#def count에서 else:에서 total += x라고 쓰는 바람에 오래 걸렸다.
#본 알고리즘에서 틀렸을 줄 알고 애꿎은 데에서 디버깅하고 있었다. 사용자 정의 함수에서 틀릴 수도 있는 건데.
#2장 만에 된되는 것은 3장 만에도 된다는 뜻이다. 2도 답이긴 하지만, 최적의 답이 아닐 뿐이다.
#lt = min(lst) 라고 초기화할 필요가 없다. 사이에 답이 있기만 하면 된다.

n, m = map(int, input().split())
lst = list(map(int, input().split()))

def count(mid):
    cnt = 1
    total = 0
    for x in lst:
        if total + x <= mid:
            total += x
        else:
            cnt += 1
            total = x
    return cnt

lt = min(lst)
rt = sum(lst)
res = sum(lst)
while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) > m:
        lt = mid + 1
    else:
        res = mid
        rt = mid - 1

print(res)