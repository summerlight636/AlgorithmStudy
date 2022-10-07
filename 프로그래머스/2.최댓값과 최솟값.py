# https://school.programmers.co.kr/learn/courses/30/lessons/12939

# list()로 묶어주는 것 깜박해서 오류 발생. (min, max 함수 사용 불가)
# answer 부분이 반복된다. => return str(min(lst)) + " " + str(max(lst))

def solution(s):
    lst = list(map(int, s.split()))

    # answer = ''
    # answer += str(min(lst))
    # answer += ' '
    # answer += str(max(lst))
    #
    # return answer

    return str(min(lst)) + " " + str(max(lst))

