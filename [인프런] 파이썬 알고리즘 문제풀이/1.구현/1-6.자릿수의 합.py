#7분+2분 = 9분

n = int(input()) #3<=n<=100
lst = list(map(int, input().split()))

def digit_sum(x):
    res = 0
    while x >= 1:
        res += x%10
        x = x//10
    return res

max_sum = 0
max_num = 0
for x in lst:
    if digit_sum(x) > max_sum:
        max_sum = digit_sum(x)
        max_num = x

print(max_num)