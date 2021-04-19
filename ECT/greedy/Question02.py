import sys
sys.stdin = open("input.txt", "rt")

s = input()
answer = int(s[0])

for i in range(1, len(s)):
    if int(s[i]) == 0 or int(s[i]) == 1 or int(s[i - 1]) == 0 or int(s[i - 1]) == 1:
        answer += int(s[i])
    else:
        answer *= int(s[i])

print(answer)

