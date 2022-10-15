#딕셔너리 정렬하는 법? ==> 그냥 cnt 테이블을 만든다...

n, m = map(int, input().split())
cnt = [[i, 0] for i in range(n+m+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j][1] += 1

cnt.sort(key=lambda x:(-x[1],x[0]))

for i in range(len(cnt)):
    if cnt[i][1] != cnt[0][1]:
        break
    else:
        print(cnt[i][0], end=' ')
