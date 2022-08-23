# 임포트

# 입력
n = int(input())
a = list(map(int, input().split()))

# 상수

# 알고리즘
# 평균 구하기
# list의 평균은 avg(arr)/len(arr
# 소수 첫째 자리에서 반올림: round
avg = round(sum(a)/len(a))
# 평균에 가장 가까운 학생
min=2147000000
for idx, x in enumerate(a):
    tmp = abs(x-avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
# 답이 2개인 경우 높은 학생 : 말 그대로 구현
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
# 번호가 빠른 학생 : 자동 적용

# 출력
print(res)
