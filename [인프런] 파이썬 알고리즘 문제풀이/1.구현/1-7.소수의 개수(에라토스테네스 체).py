# 입력
n=int(input())

#에라토스테네스 체: 2의 배수 모두 제외, 그 다음 3의 배수 모두 제외, ...
#for 문에서 step을 i로 두고 검사
ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
	if ch[i] == 0:
		cnt += 1
		for j in range(i, n+1, i):
			ch[j] = 1

print(cnt)
