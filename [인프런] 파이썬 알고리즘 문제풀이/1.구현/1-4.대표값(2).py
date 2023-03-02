n = int(input())
scores = list(map(int, input().split()))

idx_scores = []
for idx, score in enumerate(scores):
    idx_scores.append((idx, score))
idx_scores.sort(key=lambda x:(-x[1], x[0]))
print(idx_scores)

avg = int(sum(scores)/len(scores)+0.5)

target_num = idx_scores[0][0]
target_score = idx_scores[0][1]
for idx, score in idx_scores:
    if abs(avg-target_score) > abs(avg-score):
        target_num = idx+1
        target_score = score

print(avg, target_num)
