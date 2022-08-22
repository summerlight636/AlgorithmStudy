# 임포트
import sys
sys.stdin = open("input.txt", "rt")

# 입력
n, k = map(int, input().split())
# 1<=n<=10000
# 1<=k<=n

# 상수
INF = int(1e9)

# 알고리즘
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
        if count == k:
            print(i)
            break
else: #break에 의해 중단되지않고 끝까지 도는 경우 for-else 구문 사용
    print(-1)


