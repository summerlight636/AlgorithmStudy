n = int(input())

def calculate_prize():
    nun_count = [0]*6
    a, b, c = map(int, input().split())
    nun_count[a-1] += 1
    nun_count[b-1] += 1
    nun_count[c-1] += 1

    print(nun_count)

    maxCount = 0
    maxNun = 0
    for nun, count in enumerate(nun_count):
        if count >= maxCount:
            maxCount = count
            maxNun = nun+1

    if maxCount == 3:
        return 10000+maxNun*1000
    elif maxCount == 2:
        return 1000+maxNun*100
    else:
        return maxNun*100


max_prize = 0
for _ in range(n):
    prize = calculate_prize()
    print(prize)
    if max_prize < prize:
        max_prize = prize
print(max_prize)