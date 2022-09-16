lst = list(map(str, input()))
stack = []

# 1. (는 바로 넣기
# 2. )는 직전이 (일 경우 레이저: (하나 pop 하면서 res += len(stack)
# 3. 아닐 경우는 막대 끝 (하나 pop 하면서 res += 1

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