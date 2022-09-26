#원소가 복사된 횟수!!! 즉, 처음 원소가 없을 때에는 복사는 일어나지 않는다.
#2의 거듭제곱은 1부터 시작한다.
#새로운 배열이 만들어지면서, 원소가 있어야 카운트 += 기존 원소의 개수

from typing import List
import math


def solution(queries: List[List[int]]) -> int:
    cnt = 0
    dic = dict()

    for a, b in queries:
        if a not in dic.keys():
            c = 2 ** (int(math.log2(b)) + 1)
            dic[a] = (b, c)
        else:
            if dic[a][0] + b <= dic[a][1]:
                dic[a] = (dic[a][0] + b, dic[a][1])
            else:
                cnt += dic[a][0]
                dic[a] = (dic[a][0] + b, 2 ** (int(math.log2(dic[a][0] + b)) + 1))

    return cnt