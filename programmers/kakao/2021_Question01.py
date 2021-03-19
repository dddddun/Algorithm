'''import re


def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    # new_id = re.sub('~!@#$%^&*()=+[{]}:?,<>/', '', new_id)
    # new_id = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', new_id)
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
    print(new_id)
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    if new_id[0] == '.':
        if len(new_id) > 1:
            new_id = new_id[1:]

    if new_id[-1] == '.':
        new_id = new_id[:-1]

    if len(new_id) == 0:
        new_id += 'a'

    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id[0:-1]

    if len(new_id) <= 2:
        while True:
            if len(new_id) == 3:
                break
            else:
                new_id += new_id[-1]

    print(new_id)

    return answer


solution("...!@BaT#*..y.abcdefghijklm")
'''

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st