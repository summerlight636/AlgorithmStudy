#이미 오름차순으로 정렬된 리스트를 입력으로 받기 때문에 이를 활용할 수 있는 방법은 없을지 고민해봐야 함.
#.sort 는 nlogn 이기 때문에 n의 방법으로 정렬할 수 있는 다음 방법을 사용한다.

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

#포인터 변수 초기화
c = []
p1, p2 = 0, 0
while p1 < n and p2 < m:
    if a[p1] < b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 == n:
    c += b[p2:]
else:
    c += a[p1:]

print(c)

