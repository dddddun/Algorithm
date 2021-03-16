# 나의 풀이
'''
def solution(number, k):
    numbers = []
    cnt = 0
    for n in number:
        numbers.append(n)
    numbers.append('0')
    i = 0
    while True:
        if cnt == k:
            break
        if i == len(numbers)-1:
            if k != 0:
                numbers = numbers[:-k]
                break
        a = i
        b = i + 1
        if numbers[a] < numbers[b]:
            numbers.pop(a)
            i = 0
            cnt += 1
        else:
            i += 1
    numbers.pop()
    answer = ''.join(numbers)
    return answer
'''



# 해설
def solution(number, k):
    stack = []
    for num in number:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

print(solution("4177252841", 4))