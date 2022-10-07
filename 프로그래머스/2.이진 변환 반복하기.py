# https://school.programmers.co.kr/learn/courses/30/lessons/70129

# 리스트 컴프리헨션, 조건문과 반복문을 넣는 방식으로 리스트 초기화 가능(조건문은 뒤쪽에)

# 이진변환 bin(), 단 이진 변환시 0b1010 과 같이 두 글자가 할당되기 때문에 이 부분 고려해야 함.

# 문자열에서 특정 값의 개수를 반환하는 .count() 내장 함수 활용하기

# 내 풀이 수정
def solution(s):
    changed_cnt = 0
    removed_cnt = 0
    while s != "1":
        removed_cnt += len(s) - s.count("1")
        s = bin(len(s))[2:]
        changed_cnt += 1

    return [changed_cnt, removed_cnt]


# 내 풀이
def solution(s):
    changed_cnt = 0
    removed_cnt = 0
    while s != "1":
        prev_length = len(s)
        s = ''.join([x for x in s if x == '1'])
        removed_cnt += prev_length - len(s)

        s = bin(len(s))[2:]
        changed_cnt += 1

    return [changed_cnt, removed_cnt]


# 정석 풀이1
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]
