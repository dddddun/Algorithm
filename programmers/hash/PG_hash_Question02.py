# 나의 풀이 (효율성 두문제를 통과 못함)
'''
def solution(phone_book):
    dic = dict.fromkeys(phone_book, 1)
    for num in dic.keys():
        for _num in dic.keys():
            if _num.startswith(num) and _num != num:
                return False
    return True
'''

'''
def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True
'''
'''
# 해결 방법 => 길이 순으로 정렬하여 속도를 줄였다.
def solution(phoneBook):
    answer = True
    phoneBook.sort(key=lambda x: len(x))
    for i in range(len(phoneBook) - 1):
        for j in range(i + 1, len(phoneBook)):
            if phoneBook[j].startswith(phoneBook[i]):
                return False
    return answer
'''

# 딕셔너리를 사용한 정석 풀이

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer


solution(["12","123","1235","567","88"])