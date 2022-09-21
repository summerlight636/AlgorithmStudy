#3/5, 15분, 시간초과
#l이 동전의 개수인 것 부터 생소하다. 레벨 크기로 cut 할 수 있으니 더 효율적일 수도.
#순서가 의미가 없는데, 1-1-2 랑 1-2-1 한 번 더 체크하니까 비효율적인 것 아닌가?
#coin_types.sort(reverse=True) 정렬이 큰 영향을 준다. 큰 값부터 넣어야 .. .
def DFS(l, sum):
    global min_coins
    if l > min_coins:
        return
    if sum > m:
        return
    if sum == m and l < min_coins:
        min_coins = l
    else:
        for x in coin_types:
            DFS(l+1, sum+x)


n = int(input())
coin_types = list(map(int, input().split()))
coin_types.sort(reverse=True)
m = int(input())

min_coins = m
DFS(0, 0)
print(min_coins)