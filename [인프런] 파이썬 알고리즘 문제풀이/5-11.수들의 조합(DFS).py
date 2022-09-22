n, k = map(int, input().split())
lst = list(map(int, input().split()))
m = int(input())

def DFS(l, s, sum):
    global cnt
    if l == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(l+1, i+1, sum+lst[i])
cnt = 0
DFS(0, 0, 0)
print(cnt)