import sys
sys.stdin = open("input.txt", "rt")

s = input()
print(s)
right = 0
left = 0

for i in range(len(s)//2):
    left += int(s[i])

for j in range(len(s)//2, len(s)):
    right += int(s[j])

if left == right:
    print("LUCKY")
else:
    print("READY")