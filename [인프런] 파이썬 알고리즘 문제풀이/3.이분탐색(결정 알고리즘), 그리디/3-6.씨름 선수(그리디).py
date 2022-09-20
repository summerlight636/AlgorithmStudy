#왜 그리디로 풀어야 하는지 감이 안 잡힌다.

n = int(input())
lst = []
for _ in range(n):
    h, w = map(int, input().split())
    lst.append((h, w))
lst.sort(reverse=True)

cnt = 1
w_max = lst[0][1]
for i in range(1, n):
    w = lst[i][1]
    if w_max < w:
        w_max = w
        cnt += 1

print(cnt)