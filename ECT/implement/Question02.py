import sys
sys.stdin = open("input.txt", "rt")

s = input()
answer = []
cnt = 0
for st in s:
    if st.isdecimal():
        cnt += int(st)
    else:
        answer.append(st)
answer.sort()
answer = ''.join(answer) + str(cnt)
print(answer)
