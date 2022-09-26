today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

def solution(today, terms, privacies):
    ty, tm, td = map(int, today.split('.'))

    dic = dict()
    for x in terms:
        a, b = x.split()
        dic[a] = int(b)

    answer = []
    for i, x in enumerate(privacies):
        a, b = x.split()
        py, pm, pd = map(int, a.split('.'))
        pm += dic[b]
        if (ty-py)*12*28 + (tm-pm)*28 + (td-pd) >= 0:
            answer.append(i+1)
    return answer

print(solution(today, terms, privacies))