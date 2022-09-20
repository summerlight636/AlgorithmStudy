#리스트 꼬리에서 머리에 붙이기: pop과 insert활용
#굳이 temp를 쓰지 않고도 원래 mtx에서 바로 수정 가능했던 점
#행: row 열: col
n = int(input())
mtx = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for _ in range(m):
    row, direction, step = map(int, input().split())
    row -= 1
    if direction == 0: #왼쪽
        for _ in range(step):
            mtx[row].append(mtx[row].pop(0))
    else:
        for _ in range(step):
            mtx[row].insert(0, mtx[row].pop(n-1))

for x in mtx:
    print(x)

s = 0
e = n-1
total = 0
for i in range(n):
    for j in range(s, e+1):
        total += mtx[i][j]

    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(total)