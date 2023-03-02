# 문제 핵심 파악: 짧은 작업을 먼저 수행할 수록 대기시간 감소

import heapq as hq


def solution(jobs):
    jobs.sort()
    time = 0
    total = 0
    now = []

    # 반복문을 하나 더 해야하네. job을 여러 번 도는 것은 어쩔 수 없나보다.
    # 비효율적이라고 생각돼서 아닐 줄 알았다ㅠ
    s = 0
    while True:
        print(now)
        for i in (s, len(jobs)):
            if jobs[i][0] <= time:
                hq.heappush(now, (jobs[i][1], jobs[i][0]))
                s += 1 #이렇게 하면 s가 위의 변수에 영향을 준다.
            else:
                break

        if now:
            hy, hx = hq.heappop(now)
            total += hy + (time - hx)
            time += hy

        else:
            time += 1

    return (total) // len(jobs)


