# 입력
n = int(input())

# 알고리즘
# 1. 같은 눈의 개수가 몇 개인지 판별 - "중복이니까" set 활용
max_money = 0
for i in range(n):
    a, b, c = map(int, input().split())
    # '가장 큰 값' 과 같은 표현이 있을 경우 list의 sort 기능을 사용하여 단순화할 수 있지 않을까 고민해본다.
    arr = set([a, b, c])

    if len(arr) == 1:
        temp = 10000 + a * 1000
    elif len(arr) == 2:
        if a==b or a==c:
            temp = 1000 + a * 100
        else:
            temp = 1000 + b * 100
    else:
        temp = max(arr) * 100

# 2. n개의 케이스 상금 계산 후 max 값!
    if temp > max_money:
        max_money = temp

# 출력
print(max_money)
