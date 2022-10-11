#https:// school.programmers.co.kr / learn / courses / 30 / lessons / 12911?language=python3

# from collections import Counter
# Counter(string).most_common(2) :숫자 하나를 인수로 받는데 데이터 개수가 많은 순서대로 그 숫자만큼 내림차순 정렬하여 리턴함.
# a.count('찾는값')



def solution(n):
    cnt = bin(n)[2:].count('1')
    t_cnt = 0
    while cnt != t_cnt:
        n += 1
        t_cnt = bin(n)[2:].count('1')
    return n

#참고 답안1
#함수 자체에서 count=0으로 값을 넣을 수도 있구나.
#프로그래머스에서는 정해진 형태가 존재하지만, 마지막에 이렇게 count = 0과 같이 없을 경우 초기값을 설정하는 방식을 사용할 수 있다.
def nextBigNumber(n, count = 0):
    return n if bin(n).count("1") is count else nextBigNumber(n+1, bin(n).count("1") if count is 0 else count)