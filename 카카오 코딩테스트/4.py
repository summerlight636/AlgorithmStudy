numbers = [63, 111, 95, 255]

import math

def DFS1(n):
    global temp
    if n==0:
        return
    else:
        DFS1(n//2)
        temp.append(n%2)

def DFS2(temp):
    n = len(temp)
    global flag
    if n == 3:
        if temp[1] == 0:
            if temp[0] == 1 or temp[2] == 1:
                flag = 0
                return flag
            else:
                return flag

    else:
        if temp[n//2] == 0:
            if temp[(n//2-1)//2] == 1 or temp[(n-(n//2+1))//2] == 1:
                flag = 0
                return flag
        DFS2(temp[:n // 2])
        DFS2(temp[n // 2 + 1:])
    return flag


temp = []
flag = 1
def solution(numbers):
    global temp
    global flag
    answer = []
    for x in numbers:
        DFS1(x)
        pre_temp = [0]*((2**(int(math.log2(len(temp)))+1)-1)-len(temp))
        temp = pre_temp + temp
        print(temp)
        flag = 1
        answer.append(DFS2(temp))
        temp.clear()
    return answer

print(solution(numbers))