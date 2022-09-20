# 입력
n = int(input())
a = list(map(int, input().split()))

# 알고리즘

# 이 줄이 굳이 필요가 없었다. 초기 조건도 동일한 알고리즘
# score, prev = 0, 0 으로 초기화 해두고 그냥 전체 범위 알고리즘 동일하게
score, prev = a[0], a[0]
for v in a[1:]:
    if v == 0:
        prev = 0
    else:
        prev += 1
        score += prev

# 출력
print(score)
