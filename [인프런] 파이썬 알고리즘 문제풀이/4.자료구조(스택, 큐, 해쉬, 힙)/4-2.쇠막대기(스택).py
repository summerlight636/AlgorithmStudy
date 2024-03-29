# prev를 쓰지 않고 그냥 s[i], s[i-1] 을 이용할 수도 있다.
# stack.pop() 이 중복되기 때문에 한곳으로 몰 수도 있다.

lst = list(map(str, input()))
stack = []

# 1. (는 바로 넣기
# 2. )는 직전이 (일 경우 레이저: (하나 pop 하면서 res += len(stack)
# 3. 아닐 경우는 막대 끝 (하나 pop 하면서 res += 1

''' 모범 답안 
s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(':
            cnt+=len(stack)
        else:
            cnt+=1
print(cnt)
'''

res = 0
prev = ''
for x in lst:
    if x == '(':
        stack.append(x)
    else:
        if prev == '(':
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1
    prev = x

print(res)

