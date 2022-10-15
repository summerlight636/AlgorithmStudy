#*0의 개수 만큼 필요하다 => 처음 값에서 0을 만날 때마다 lst[i] -= 1 이렇게 => 아예 이렇게 주어진 리스트에서 값을 하나하나 줄이는 것
#인덱스 값이랑 실제 숫자 값이랑 동일하게 하고 싶으면, lst.insert(0, 0)을 해주는 것이 편하다.
n = int(input())
lst = list(map(int, input().split()))

res = [0]*n
for i in range(n):
    for j in range(n):
        if lst[i] == 0 and res[j] == 0:
            res[j] = i+1
            break
        elif res[j] == 0:
            lst[i] -= 1

for x in res:
    print(x, end=' ')

