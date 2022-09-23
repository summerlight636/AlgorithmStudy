#문제를 이해를 못했다. 같은 무게의 추를 여러 번 담을 수 있는건가?
#문제를 잘못 이해할 경우 잘못된 알고리즘을 작성하는데 드는 시간이 엄청나게 소모된다.
#심지어 아예 불가능한 알고리즘에 대해 고민하게 되어 끝이 나지 않을 수도 있다.
#그러니, 문제를 꼭 정확하게 이해하고, 세세한 조건들도 꼼꼼히 보자.
#양팔 저울이므로 왼쪽 +1 오른쪽 -1 아무데도 안놓음 0 이렇게 처리할 수 있다.

def DFS(l, sum):
    if l == k:
        if sum > 0:
            res[sum] = 1
    else:
        DFS(l+1, sum+lst[l])
        DFS(l+1, sum-lst[l])
        DFS(l+1, sum)

k = int(input()) #3<=k<=13
lst = list(map(int, input().split())) #1~200000

res = [0]*(sum(lst)+1)
res[0] = 1
DFS(0, 0)
cnt = 0
for i in range(sum(lst)+1):
    if res[i] != 1:
        cnt += 1
print(cnt)