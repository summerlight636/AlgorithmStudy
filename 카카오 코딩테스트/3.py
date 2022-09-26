from itertools import product

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

def solution(users, emoticons):
    max_plus = 0
    max_price = 0
    for temp in (product([40, 30, 20, 10], repeat=len(emoticons))):
        temp_plus = 0
        temp_price = 0
        for sale, price in users:
            total = 0
            for i, t in enumerate(temp):
                if t >= sale:
                    total += emoticons[i] * (100-t)/100
            if total >= price:
                temp_plus += 1
            else:
                temp_price += total
        if max_plus < temp_plus:
            max_plus = temp_plus
            max_price = temp_price
        elif max_plus == temp_plus:
            if max_price < temp_price:
                max_price = temp_price
    result = []
    result.append(max_plus)
    result.append(int(max_price))
    return result

print(solution(users,emoticons))