import math

def solution(brown, yellow):
    answer = []
    y_divisor = []
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            y_divisor.append([i, yellow//i])
    for x, y in y_divisor:
        if 2*x + 2*y + 4 == brown:
            answer.append(y+2)
            answer.append(x+2)
    return answer

solution(24, 24)