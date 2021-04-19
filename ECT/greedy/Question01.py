import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
travelers = list(map(int, input().split()))
travelers.sort()
member_cnt = 0
result = 0

for traveler in travelers:
    member_cnt += 1
    if traveler <= member_cnt:
        result += 1
        cnt = 0

print(result)