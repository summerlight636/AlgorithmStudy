# Object of type set is not JSON serializable: set 자료형을 return 하려고 하니까 오류 발생 // 이유는 검색해도 안 나온다 ㅠㅠ
# solution 함수의 변수를 사용하려면 그대로 dfs의 변수에 넣어주는 수 밖에 없다.. (여기서 numbers 처럼)
# 같은 수가 여러 개 있을 수도 있으니, 한 번만 계산하기 위해 걸러내는 과정
# Object of type set is not JSON serializable: set 자료형을 return 하려고 하니까 오류 발생 : 그래서 list로 바꾸어서 반환해주었다.
# remove를 사용하기 위해서, number를 리스트로 바꾸어주기

selected_numbers = set()


def dfs(l, res, numbers):  # solution 함수의 변수를 사용하려면 그대로 dfs의 변수에 넣어주는 수 밖에 없다.. (여기서 numbers 처럼)
    global selected_numbers

    if len(numbers) == 0:
        selected_numbers.add(res)
    else:
        # 같은 수가 여러 개 있을 수도 있으니, 한 번만 계산하기 위해 걸러내는 과정
        temp = set(numbers)

        for x in temp:
            numbers.remove(x)
            dfs(l + 1, res + x, numbers)
            dfs(l + 1, res, numbers)
            numbers.append(x)


def isPrime(n):
    ch = [0] * (n + 1)
    prime = set()
    for i in range(2, n + 1):
        if ch[i] == 0:
            prime.add(i)
            for j in range(2 * i, n + 1, i):
                ch[j] = 1

    return list(
        prime)  # Object of type set is not JSON serializable: set 자료형을 return 하려고 하니까 오류 발생 : 그래서 list로 바꾸어서 반환해주었다.


def solution(numbers):
    global selected_numbers

    # remove를 사용하기 위해서, number를 리스트로 바꾸어주기
    numbers = [x for x in numbers]

    dfs(0, "", numbers)
    selected_numbers = set(map(int, selected_numbers - {''}))
    answer = selected_numbers & set(isPrime(max(selected_numbers)))

    return len(answer)