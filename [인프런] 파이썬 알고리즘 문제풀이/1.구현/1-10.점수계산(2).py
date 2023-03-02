n = int(input())
lst = map(int, input().split())

prev_x = 0
totalScore = 0
for x in lst:
    if x==1:
        totalScore += prev_x + 1
        prev_x = prev_x + 1
    else: #x가 0일 때
        prev_x = 0

print(totalScore)