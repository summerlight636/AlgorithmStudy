#특정 테케에서만 시간 초과가 나온다: 조금 발전시켜보자
#level 단계를 스킵할 수 있도록 변수 추가(tsum)
#total - tsum : 미래의 노드의 합을 표현할 수 있다!!

def DFS(l, sum, tsum):
    global max_weight
    #시간 단축을 위한 조건1
    if sum + (total-tsum) < max_weight:
        return
    #시간 단축을 위한 조건2
    if sum > c:
        return
    if l == n:
        max_weight = max(max_weight, sum)
    else:
        DFS(l+1, sum+weight[l], tsum+weight[l])
        DFS(l+1, sum, tsum+weight[l])

c, n = map(int, input().split())
weight = []
for _ in range(n):
    weight.append(int(input()))

max_weight = 0
total = sum(weight)
DFS(0, 0, 0)
print(max_weight)