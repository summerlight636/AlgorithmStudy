#이분 검색을 언제 사용하는가?-> '결정 알고리즘' 이라는 결정론에서.
#이런 특징이 있다-> 찾고자하는 답이 특정 범위 안에 있다는 것을 바로 알 수 있다.
#중앙값을 정해놓고 그 값이 답으로 유효하냐 아니냐
#count() 함수로 따로 빼는 것이 깔끔하다.
#n이라고 써야 하는 곳에 입력 예제의 11을 써버리는 실수!


k, n = map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))

def count(len):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt

lt = 1
rt = max(line)
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) < n:
        rt = mid - 1
    else:
        res = mid
        lt = mid + 1
print(res)
