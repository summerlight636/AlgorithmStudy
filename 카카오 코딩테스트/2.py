from collections import deque
cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]
def solution(cap, n, deliveries, pickups):
    deliveries = deque(deliveries)
    pickups = deque(pickups)

    while deliveries[-1] == 0:
        deliveries.pop()
    while pickups[-1] == 0:
        pickups.pop()

    total = 0
    while deliveries or pickups:
        temp = cap
        total += 2*max(len(deliveries), len(pickups))
        while deliveries and temp-deliveries[-1] >= 0:
            temp -= deliveries.pop()
        if deliveries:
            deliveries.append(deliveries.pop()-temp)
        temp = cap
        while pickups and temp-pickups[-1] >= 0:
            temp -= pickups.pop()
        if pickups:
            pickups.append(pickups.pop()-temp)
    return total

print(solution(cap, n, deliveries, pickups))