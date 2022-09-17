#후위식 연산은 직관적이네.
s = list(str(input()))

stack = []
for x in s:
    if x.isdigit():
        stack.append(int(x))
    else:
        b = stack.pop()
        a = stack.pop()
        if x == '+':
            stack.append(a+b)
        elif x == '-':
            stack.append(a-b)
        elif x == '/':
            stack.append(a/b)
        else:
            stack.append(a*b)
print(stack[0])