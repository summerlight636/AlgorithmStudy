#풀이법이 생각이 안난다. (단순한 것 밖에) => 실제로 단순한 문제였다.
l = int(input())
lst = list(map(int, input().split()))
m = int(input())

lst.sort()

for i in range(m):
    if lst[0] == lst[-1]:
        break
    else:
        lst[0] += 1
        lst[-1] -= 1
        lst.sort()

print(lst[-1] - lst[0])