from itertools import combinations
from collections import Counter


def solution(orders, course):
    result = []

    for cour in course:
        order_comb = []
        for order in orders:
            if cour <= len(order):
                order_comb += combinations(sorted(order), cour)
        most_ordered = Counter(order_comb).most_common()
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]
    answer = [''.join(v) for v in sorted(result)]
    return answer


solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
