n = int(input())
numbers = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x>0:
        res = res*10 + x%10
        x = x//10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

for number in numbers:
    reversed_number = reverse(number)
    if isPrime(reversed_number):
        print(reversed_number, end=' ')