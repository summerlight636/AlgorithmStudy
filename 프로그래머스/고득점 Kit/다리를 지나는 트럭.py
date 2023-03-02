# 구현을 못하겠다... => 구현은 제대로 했지만 '다리에 완전히 오르지 않은 트럭의 무게는 무시한다' 항목을 잘못 이해함

from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    trucks = deque([])

    time = 0
    now_weight = 0
    while True:
        if trucks and trucks[0][0] + bridge_length == time:
            now_weight -= trucks[0][1]
            trucks.popleft()
        if truck_weights and now_weight + truck_weights[0] <= weight:
            now_weight += truck_weights[0]
            trucks.append((time, truck_weights.popleft()))
        time += 1
        if not trucks:
            break
    return time
