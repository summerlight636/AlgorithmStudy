#dict1.get('A', 0): 해당 키 값이 있으면 dict[A] 를 리턴, 없으면 0을 리턴하는 함수
#두 딕셔너리 내용물은 같은데 순서가 다른 경우? 모든 key에 대해 직접 for문으로 확인
#같다, 틀리다= 어떤 것의 개수가 +- 했을 때 결과가 0이 된다

s1 = input()
s2 = input()
sH = dict()
for x in s1:
    sH[x] = sH.get(x, 0) + 1
for x in s2:
    sH[x] = sH.get(x, 0) - 1
for key in sH.keys():
    if sH[key] != 0:
        print("NO")
        break
else:
    print("YES")

'''
s1_dict = dict()
for v in s1:
    s1_dict[v] = s1_dict.get(v, 0) + 1

s2_dict = dict()
for v in s2:
    s2_dict[v] = s2_dict.get(v, 0) + 1


for i in s1_dict.keys():
    if i in s2_dict.keys():
        if s1_dict[i] != s2_dict[i]:
            print("NO")
            break
    else:
        print("NO)
        break
else:
    print("YES")
'''

