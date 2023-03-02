#6분
#n이 100으로 작으므로, 10^6인 N^3 까지는 괜찮을 것이다. (효율 크게 따지지 않아도 된다)
#set은 append가 아닌 add로 값을 추가해주어야 한다.
#set인 상태로는 정렬을 할 수 없으므로(set은 순서가 없고, 중복이 없는 특징을 가지므로) 리스트로 변환 후 정렬

n, k = map(int, input().split())
cards = list(map(int, input().split()))

res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(cards[i]+cards[j]+cards[m])

res = list(res)
res.sort(reverse=True)
print(res[k-1])
