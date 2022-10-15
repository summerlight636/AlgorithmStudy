#포인터 잡을때 lt, rt 와 같이 잡는다. (무조건 lt < rt 이기 때문)
#p1, p2 와 같이 잡을 때에는 서로 대소관계가 유지되지 않는 경우에 쓴다.

#시간초과 나온 코드: 이유 질문/ 나중에 확인하기!/ n^2 의 알고리즘이기 때문이다.
n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
for lt in range(n):
    rt = lt + 1
    tot = 0
    while tot < m and rt <= n:
        tot = sum(a[lt:rt])
        if tot == m:
            cnt += 1
            break
        rt += 1

print(cnt)

# 새로 짠 코드
# 2-5.수들의 합
#
# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))
#
# sum = 0
# cnt = 0
# for i in range(n):
#     sum = numbers[i]
#     if sum == m:
#         cnt += 1
#         continue
#
#     for j in range(i+1, n):
#         sum += numbers[j]
#         if sum == m:
#             cnt += 1
#             break
#         elif sum > m:
#             break
#
# print(cnt)
