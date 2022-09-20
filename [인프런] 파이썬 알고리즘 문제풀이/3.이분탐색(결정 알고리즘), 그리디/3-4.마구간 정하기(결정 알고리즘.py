#이게 왜 결정 알고리즘인지부터 알아채기 어렵다.
#rt = lst[n-1] 으로 잡으면 된다. (최댓값 말고)
#정렬된 리스트에서 완전탐색 하는 방법이라고 생각하자. 
#결정 알고리즘의 형식은 계속 똑같다.
#while lt<=rt:
#mid =
#if(True):
#res =
#lt =
#if(False):
#rt =


n, c = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
def check(lst, mid):
    cnt = 1
    prev = lst[0]
    for x in lst:
        if x >= prev + mid:
            cnt += 1
            prev = x
        if cnt == c:
            return True
    return False


lt = 1
rt = lst[n-1]
res = 1

while lt <= rt:
    mid = (lt+rt)//2
    if check(lst, mid):
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)