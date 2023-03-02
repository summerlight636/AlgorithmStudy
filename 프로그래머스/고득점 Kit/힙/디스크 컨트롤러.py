# sort 시 reverse=True로 한 뒤, pop() 을 하는 것이 더 시간 단축에는 도움이 될 것이라는 의견
# tasks 라는 변수를 따로 선언하는 게 더 적절했을 듯 하다.
# 구하는 값: total 보다는 total_response_time 이 적절한 변수명
# 행동 기준: 시간
# 시간에 맞는 행동1: 그 시간에 시작 가능한 작업 큐에 넣기
# 시간에 맞는 행동2: 큐 중에서 제일 작업 시간 짧은 것 빼서 작업 / 비어 있다면 대기(current_time+=1)
from collections import deque as dq
import heapq as hq

def solution(jobs):
    job_length = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1])) # sort 시 reverse=True로 한 뒤, pop() 을 하는 것이 더 시간 단축에는 도움이 될 것이라는 의견
    jobs = dq(jobs) # tasks 라는 변수를 따로 선언하는 게 더 적절했을 듯 하다.

    total = 0  # 구하는 값: total 보다는 total_response_time 이 적절한 변수명
    current_time = 0  # 행동 기준: 시간
    todo = []
    while jobs or todo:
        # 시간에 맞는 행동1: 그 시간에 시작 가능한 작업 큐에 넣기
        while jobs and jobs[0][0] <= current_time:
            hq.heappush(todo, (jobs[0][1], jobs[0][0]))
            jobs.popleft()
        # 시간에 맞는 행동2: 큐 중에서 제일 작업 시간 짧은 것 빼서 작업 / 비어 있다면 대기(current_time+=1)
        if todo:
            a, b = hq.heappop(todo)
            current_time += a
            total += current_time - b
        else:
            current_time += 1

    return total // job_length

#참고 답안
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)
