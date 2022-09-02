# 대소문자를 구별하지 않는다 라는 조건을 누락. s.upper()
# 새로운 함수를 만들 필요도 없이, 단순하게 s == s[::-1] 을 이용할 수 있었음.
# 문자열 슬라이싱/정렬 등 기본 기능을 활용했어야 했다.
# 임포트
def check(str):
    for i in range(len(str)//2):
        if str[i] != str[-(i+1)]:
            print("NO")
            break
    else:
        print("YES")

# 입력
n = int(input())
arr = []
for i in range(n):
    arr.append(input().upper())

# 알고리즘
for i in range(n):
    print("#"+str(i+1), end=' ')
    check(arr[i])
