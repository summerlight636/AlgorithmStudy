#LIFO 해야겠다 싶으면 스택 생각하기
#후위 표기식 자체가 잘 이해가 안됨 -> 다시 시도


stack = []
for i in len(s):
    if x.isdigit:
        res += x
    else:
        if s[i] == '(':
            stack.append(s[i])

'''모범 답안
a=input()
stack=[]
res=''
for x in a:
    if x.isdecimal():
        res+=x
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)
'''