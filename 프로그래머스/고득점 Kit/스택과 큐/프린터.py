from collections import deque
def solution(priorities, location):
    priorities = deque(priorities)
    index = deque([i for i in range(len(priorities))])
    maximum = max(priorities)
    cnt = 0
    while priorities:
        if priorities[0] < maximum:
            priorities.append(priorities.popleft())
            index.append(index.popleft())
        else:
            cnt += 1
            priorities.popleft()
            if index.popleft() == location:
                print(cnt)
                break
            maximum = max(priorities)
    return cnt