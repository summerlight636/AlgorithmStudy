# 입력
n = int(input())
a = list(map(int, input().split()))

# 알고리즘
# 숫자 뒤집기
def reverse(x):
    x = str(x)[len(str(x))::-1]
    while x[0] == '0':
        x = x[1:]
    return int(x)

# 소수 판별
# 수가 커지면 .. ?
def isPrime(x):
    #예외 사항 안 쓸 뻔했다~!
    if x == 1:
        return False

    #소수 판별할 때 절반만 확인하면 된다~!
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:
        return True

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')

