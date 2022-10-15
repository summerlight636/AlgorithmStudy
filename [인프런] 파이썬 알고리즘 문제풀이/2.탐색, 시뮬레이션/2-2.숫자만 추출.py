# 리스트를 문자열으로 ?
# for 문에서 값은 x, 인덱스 값은 i로 통일 하기
# .isdecimal() 을 이용하면 숫자인지 판별 가능
#* 첫자리 0은 무시: res = res*10 + int(x) 를 이용하면 앞자리 0을 자연스럽게 제거할 수 있다.

# 입력
s = input()

# 알고리즘
# 1. 최종 숫자
# 숫자만 추출
num = 0
for x in s:
    if x.isalpha():
        continue
    else:
        num = num*10 + int(x)

# 첫 자리 0은 무시
'''
while temp[0] == '0':
    temp = temp[1:]
    if temp == "":
        print(0)
'''

# 2. 약수의 개수 / n = 10^8 인데 그냥 O(n)써도 되나 ?
cnt = 0
for i in range(1, num+1):
    if num % i == 0:
        cnt += 1

# 출력
print(num)
print(cnt)
