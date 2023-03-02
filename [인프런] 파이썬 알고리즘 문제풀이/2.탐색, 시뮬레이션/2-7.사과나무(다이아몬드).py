#다이아몬드 모양 어떻게 구현 할 지 바로 나오도록
#*s, e 시작점, 끝점을 명시하면 직관적으로 표현할 수 있다.
#*j의 범위를 i와 n으로만 표현하려는 생각을 버리자.

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

total = 0

s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        total += arr[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(total)