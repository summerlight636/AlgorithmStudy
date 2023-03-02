n = int(input())
numbers = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x>0:
        sum += x%10
        x = x//10
    return sum

max_number = numbers[0]
max_sum = digit_sum(max_number)
for number in numbers:
    if max_sum < digit_sum(number):
        max_number = number
        max_sum = digit_sum(number)

print(max_number)