# https://school.programmers.co.kr/learn/courses/30/lessons/12951

# 문자열 상태 그대로에서 값만 바꿀 수 있나?
# 'str' object does not support item assignment : 문자열은 수정이 불가능한 자료구조

# 실행한 결괏값 "3people UnFollowed Me"이 기댓값 "3people Unfollowed Me"과 다릅니다.
# 왜 중간의 값이 바뀌었지? 바뀐 것이 아니라, 원래 입력 값이 대문자였고 그것을 소문자로 바꾸는 과정이 필요했던 것(문제를 꼼꼼히 읽기.)


# 문자열 함수 s.title() : 숫자는 무시하고, (숫자 다음 글자도)첫 글자만 대문자로 바꾸어주는 함수
# def solution(s):
#     return s.title()

# ' '.join(리스트) 은 리스트의 값을 문자열로 반환해주는 방법으로 자주 활용됨
# 리스트 값을 가공해서 새로운 리스트를 만들 수 있는 [x[0] for x in 리스트] 와 같은 표현 익숙해지기
def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])

# 내 풀이
# def solution(s):
#     answer = ''
#     if s[0].isalpha():
#         answer += s[0].upper()
#     else:
#         answer += s[0]
#     for i in range(1, len(s)):
#         if s[i-1] == " " and s[i].isalpha():
#             answer += s[i].upper()
#         else:
#             answer += s[i].lower()
#     return answer