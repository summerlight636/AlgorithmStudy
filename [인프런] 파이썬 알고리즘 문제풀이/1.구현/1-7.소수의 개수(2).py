# list와 set 속도 차이가 심하네. set으로 바꾸니까 시간 제한 문제를 해결할 수 있었다
n = int(input())

res = []
checked = set()
for i in range(2, n+1):
    if i not in checked:
        res.append(i)
        for j in range(i, n+1, i):
            checked.add(j)

print(len(res))