#2차원 배열 선언 a = [list(map(int, input().split())) for _ in range(n)]
#행 탐색과 열 탐색은 순서만 바꾸면 된다.
for i in range(n):
    sum1 = 0
    sum2 = 0 
    for j in range(n):
        sum1 += a[i][j] //i행의 합
        sum2 += a[j][i] //j행의 합

#정답
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
largest=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
print(largest)

