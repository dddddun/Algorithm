from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while bridge:
        time += 1
        bridge.popleft()
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    print(time)
    return time
'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    time = 0
    bridge_weight = 0
    while len(bridge) != 0:
        out = bridge.popleft()
        bridge_weight -= out
        time += 1
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                left = truck_weights.popleft()
                bridge_weight += left
                bridge.append(left)
            else:
                bridge.append(0)
    return time
'''
'''
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length

    while len(bridge) != 0:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    print(time)
    return time
'''

solution(2, 10, [7, 4, 5, 6])