def solution(clothes):
    answer = 1
    dic = dict()
    for x, y in clothes:
        if y in dic:
            dic[y] += 1
        else:
            dic[y] = 2
    combi = list(dic.values())
    for x in combi:
        answer *= x
    return answer - 1


solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])

'''
import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1
'''

'''
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
'''