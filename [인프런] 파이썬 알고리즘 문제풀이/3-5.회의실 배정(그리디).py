#그리디 문제는 정렬이다.
#정렬한 후 그 순간의 최선의 선택을 하는 것이 솔루션
#어떤 것을 기준으로 정렬? => 끝나는 시간으로 정렬
#list.sort(key = lambda x: (x[1], [0])) 기준 두 개 해야한다!

#lst = sorted(lst, key = lambda x : x[1]) 을
#lst.sort(key=lambda x : (x[1], x[0])) 으로 수정!

#if 하면 긍정적인 조건을 먼저 작성 => 직관적으로 이해하기 쉽게. 

n = int(input())
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append((s, e))

#lst = sorted(lst, key = lambda x : x[1])
lst.sort(key=lambda x : (x[1], x[0]))

cnt = 1
prev_e = lst[0][1]
for i in range(1, n):
    s = lst[i][0]
    e = lst[i][1]

    if s < prev_e:
        continue
    else:
        cnt += 1
        prev_e = e

print(cnt)
