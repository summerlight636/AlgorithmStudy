#정답
#이미 중간 영역은 구해진 값을 재활용하면 되는데, 내가 원래 짰던 코드는 이미 구한 중간 값까지 싹 다시 더해서 구하기 때문에 비효율 => 시간초과
#중간 값들은 변하지 않고, 양 끝 값만 변하는 경우 => 포인터 활용
n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0]
cnt=0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)