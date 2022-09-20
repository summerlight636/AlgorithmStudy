#체크리스트 ch1, ch2, ch3 을 만들어서 sum을 이용해 1의 개수 합을 구하여 모든 조건 만족했는지 확인
#set을 이용하는 방법은 1~9 외의 값이 들어올 수도 있기 때문에 오류 발생 가능성

mtx = [list(map(int, input().split())) for _ in range(9)]

def check(mtx):
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[mtx[i][j]] = 1
            ch2[mtx[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):
                for l in range(3):
                    ch3[mtx[3*i+k][3*j+l]] = 1
            if sum(ch3) != 9:
                return False
    else:
        return True

if check(mtx):
    print("YES")
else:
    print("NO")