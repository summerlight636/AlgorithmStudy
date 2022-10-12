# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    dic = dict()

    i = 1
    for idx, x in enumerate(words):
        if x not in dic.keys():
            dic[x] = 1
            if idx > 0 and words[idx - 1][-1] != x[0]:
                return [i % n if i % n != 0 else n, i // n + 1 if i % n != 0 else i // n]
        else:
            return [i % n if i % n != 0 else n, i // n + 1 if i % n != 0 else i // n]
            break
        i += 1

    else:
        return [0, 0]


# 참고 답안
# i=0 에서 오류가 발생할 가능성이 없기 때문에 그냥 i=1 부터 확인
# 더 간단하게 i%n + 1 과 i//n +1 으로 표현할 수 있었는데 복잡하게 생각했다.
# =>> 처음 인덱스를 1, 2, 3... 으로 잡으면 복잡하게 표현할 수 밖에 없다 
# 몫과 나머지를 이용할 경우, 인덱스가 0, 1, 2... 가 되도록 표현해야 자연스럽게 표현된다. 
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p - 1][-1] or words[p] in words[:p]: return [(p % n) + 1, (p // n) + 1]
    else:
        return [0, 0]