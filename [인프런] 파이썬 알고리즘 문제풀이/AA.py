#리스트 회문: tmp == tmp[::-1] 이용할 수 있음!!(가로 방향만 가능)
#if k==1: cnt += 1 같이 하지말고, break 안된 경우를 말하는 else: 문 사용
mtx = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for j in range(3):
        for k in range(2):
            if mtx[i][j+k] != mtx[i][j+4-k]:
                break
        else:
            cnt += 1
        for k in range(2):
            if mtx[j+k][i] != mtx[j+4-k][i] :
                break
        else:
            cnt += 1

print(cnt)